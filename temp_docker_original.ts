import Docker from 'dockerode';

// Initialize Docker client
// When running inside a container with /var/run/docker.sock mounted, this works automatically.
const docker = new Docker({ socketPath: '/var/run/docker.sock' });

export interface AppCard {
    id: string;
    name: string;
    group: string;
    icon: string;
    description: string;
    url: string;
    status: string;
    state: string;
}

export async function getRunningContainers(): Promise<AppCard[]> {
    try {
        const containers = await docker.listContainers({ all: true });

        return containers
            .filter((container) => !container.Names.some((n) => n.includes('kooldock-kooldock')))
            .map((container) => {
                // Extract labels
                const labels = container.Labels || {};
                const name = labels['kool.name'] || container.Names[0].replace('/', '');
                const group = labels['kool.group'] || 'Applications';
                // Determine Icon
                let icon = labels['kool.icon'];
                if (!icon) {
                    const lowerName = name.toLowerCase();

                    const ICON_MAPPING: Record<string, string> = {
                        'transcript': 'FileText',
                        'popcorn': 'Clapperboard',
                        'movie': 'Film',
                        'film': 'Film',
                        'plex': 'Film',
                        'jellyfin': 'Film',
                        'radarr': 'Film',
                        'sonarr': 'Film',
                        'music': 'Music',
                        'lidarr': 'Music',
                        'spotify': 'Music',
                        'download': 'Download',
                        'transmission': 'Download',
                        'qbittorrent': 'Download',
                        'sabnzbd': 'Download',
                        'db': 'Database',
                        'database': 'Database',
                        'postgres': 'Database',
                        'mysql': 'Database',
                        'mongo': 'Database',
                        'redis': 'Database',
                        'portainer': 'Container',
                        'docker': 'Container',
                        'nginx': 'Network',
                        'proxy': 'Network',
                        'traefik': 'Network',
                        'home': 'Home',
                        'dashboard': 'LayoutDashboard',
                        'homepage': 'Home',
                        'monitor': 'Activity',
                        'grafana': 'Activity',
                        'prometheus': 'Activity',
                        'auth': 'Lock',
                        'login': 'Lock',
                        'keycloak': 'Lock',
                        'authelia': 'Lock',
                        'code': 'Code',
                        'git': 'Code',
                        'gitlab': 'Code',
                        'gitea': 'Code',
                        'cloud': 'Cloud',
                        'nextcloud': 'Cloud',
                        'owncloud': 'Cloud',
                        'mail': 'Mail',
                        'smtp': 'Mail',
                        'chat': 'MessageCircle',
                        'discord': 'MessageCircle',
                        'slack': 'MessageCircle',
                        'mattermost': 'MessageCircle',
                        'game': 'Gamepad2',
                        'minecraft': 'Gamepad2',
                        'steam': 'Gamepad2',
                        'n8n': 'Workflow',
                        'automation': 'Workflow',
                        'builder': 'Hammer',
                        'studio': 'Palette',
                    };

                    for (const [keyword, iconName] of Object.entries(ICON_MAPPING)) {
                        if (lowerName.includes(keyword)) {
                            icon = iconName;
                            break;
                        }
                    }

                    if (!icon) {
                        icon = 'Box';
                    }
                }

                // Determine URL
                // Priority: kool.url label > http://<container-name>.kooldocker.local
                // Determine Description
                let description = labels['kool.description'];
                if (!description) {
                    const lowerName = name.toLowerCase();
                    const DESCRIPTION_MAPPING: Record<string, string> = {
                        'popcorn': 'Movie & TV tracker',
                        'studio': 'Creative design studio',
                        'dashboard': 'System dashboard',
                        'transcript': 'AI Transcription service',
                        'portainer': 'Container management',
                        'nginx': 'Web server & proxy',
                        'traefik': 'Edge router & proxy',
                        'plex': 'Media server',
                        'jellyfin': 'Media server',
                        'sonarr': 'TV show automation',
                        'radarr': 'Movie automation',
                        'lidarr': 'Music automation',
                        'transmission': 'BitTorrent client',
                        'qbittorrent': 'BitTorrent client',
                        'postgres': 'Relational database',
                        'mysql': 'Relational database',
                        'redis': 'In-memory data store',
                        'grafana': 'Analytics & monitoring',
                        'prometheus': 'Monitoring system',
                        'n8n': 'Workflow automation',
                        'nextcloud': 'Productivity platform',
                        'home': 'Home automation',
                        'gitea': 'Git service',
                        'gitlab': 'DevOps platform',
                        'uptime': 'Uptime monitoring',
                        'kuma': 'Uptime monitoring',
                        'authelia': 'Authentication server',
                        'keycloak': 'Identity and access management',
                    };

                    for (const [keyword, desc] of Object.entries(DESCRIPTION_MAPPING)) {
                        if (lowerName.includes(keyword)) {
                            description = desc;
                            break;
                        }
                    }
                }

                // Determine URL
                // Priority: kool.url label > http://kooldock.local:<public-port>
                let url = labels['kool.url'];

                if (!url) {
                    const portMapping = container.Ports.find((p) => p.PublicPort);
                    if (portMapping) {
                        url = `http://kooldock.local:${portMapping.PublicPort}`;
                    } else {
                        // Fallback if no port is exposed
                        url = '#';
                    }
                }

                return {
                    id: container.Id,
                    name,
                    group,
                    icon,
                    description: description || '',
                    url,
                    status: container.Status,
                    state: container.State,
                };
            });
    } catch (error) {
        console.error('Error fetching containers:', error);
        return [];
    }
}
