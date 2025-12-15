#!/bin/bash

# Configuración
BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DB_CONTAINER="postgresql"
DB_USER="odoo"
DB_NAME="postgres" # O el nombre de tu BD si es diferente
WEB_DATA_DIR="./odoo-web-data"

# Crear directorio de backups si no existe
mkdir -p "$BACKUP_DIR"

echo "Iniciando backup..."

# 1. Backup de la Base de Datos (SQL)
echo "1. Exportando base de datos..."
docker exec -t $DB_CONTAINER pg_dumpall -c -U $DB_USER > "$BACKUP_DIR/odoo_db_$TIMESTAMP.sql"

# 2. Backup del Filestore (Archivos adjuntos)
echo "2. Comprimiendo filestore..."
tar -czf "$BACKUP_DIR/odoo_filestore_$TIMESTAMP.tar.gz" -C "$WEB_DATA_DIR" .

echo "✅ Backup completado en $BACKUP_DIR"
echo "   - DB: odoo_db_$TIMESTAMP.sql"
echo "   - Files: odoo_filestore_$TIMESTAMP.tar.gz"
