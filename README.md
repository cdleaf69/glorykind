# Glorykind

Catholic Christmas storefront with 50 products and a separate supplier management panel. Plain HTML, CSS and JavaScript; no build step or dependencies.

## Repository layout

- `docs/` — public website, product images and catalogue. This is the GitHub Pages publishing folder.
- `supplier-admin/` — supplier links, costing, notes and sourcing information. Kept outside the public website folder.
- `serve.py` — optional local server.

## Upload to GitHub

Extract this archive and upload its contents to the repository root. Include the hidden `.gitignore`, `.gitattributes` and `docs/.nojekyll` files. Do not upload the ZIP itself.

## Publish the shop with GitHub Pages

In the repository Settings, open Pages. Choose Deploy from a branch, select your main branch and `/docs`, then Save. Use the website address shown by GitHub once deployment completes. All storefront paths are relative, so repository subpaths work without editing the site.

Only `docs/` is published by that configuration. The supplier panel is included in the repository but excluded from the Pages website. A public repository still exposes every committed file, including supplier data. Use a private repository if that information should remain private; Pages availability for private repositories depends on your account.

## Run locally

Install Python 3 and run `python serve.py` from this folder.

- Shop: http://localhost:8767/
- Supplier panel: http://localhost:8767/admin/

## Edit the website

Edit HTML pages, `docs/styles.css`, and `docs/app.js`. Products are in `docs/assets/products.json`. Supplier records are in `supplier-admin/assets/suppliers.json`. Product images are bundled locally; fonts load from Google Fonts.

## Ordering and administration

Search, sorting, filters, pagination, favorites and the shopping bag work. Checkout displays “Online ordering opens soon.” Payments, server-side orders, shipping calculations, tax and fulfillment are not connected.

The supplier panel stores notes and costing in each browser. It has no authentication or shared database. Publish it separately behind authentication if remote access is needed. Change its Open storefront link to your published shop URL when hosting separately. Confirm supplier samples, photo permissions, prices and fulfillment before sales.
