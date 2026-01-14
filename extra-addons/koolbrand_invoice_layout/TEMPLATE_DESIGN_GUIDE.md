# Koolbrand Invoice Design Guide

## Overview
This module (`koolbrand_invoice_layout`) defines the custom look for "Brand Experience YA" invoices.
It relies on Odoo's `report.layout` but **overrides** the `account.report_invoice_document` template body directly (`koolbrand_body_extension`) to control the table, fonts, and colors.

## Key Files
- `views/report_invoice.xml`: The detailed HTML/QWeb structure of the invoice body.
    - Uses `inherit_id="account.report_invoice_document"`.
    - **Crucial**: It sets the `<thead>` background color to `#A3D16D` (Green).
- `data/report_layout.xml`: Registers "Koolbrand Layout" in the system so it can be selected in General Settings > Document Layout.

## Colors
- **Header Green**: `#A3D16D`
- **Text Color**: `#555`

## Fonts
- **Standard**: 'Montserrat', sans-serif

## Deployment
When modifying this:
1. Edit `views/report_invoice.xml`.
2. Upgrade the module in Odoo (Apps > koolbrand_invoice_layout > Upgrade).
3. Check a PDF printout.
