FROM odoo:latest
USER root
COPY ./requirements.txt /etc/odoo/requirements.txt
RUN pip3 install --break-system-packages -r /etc/odoo/requirements.txt && rm -rf /root/.cache/pip
USER odoo