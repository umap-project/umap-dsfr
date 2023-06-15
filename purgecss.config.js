module.exports = {
  content: ['umap_dsfr/templates/umap/*.html'],
  css: [
    'node_modules/@gouvfr/dsfr/dist/dsfr.min.css',
    'node_modules/@gouvfr/dsfr/dist/utility/icons/icons.min.css'
  ],
  safelist: [
    'body', // Useful to keep the Marianne font.
  ],
  output: 'umap_dsfr/static/umap/dsfr-lite/'
}
