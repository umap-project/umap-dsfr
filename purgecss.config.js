module.exports = {
	content: ["umap_dsfr/templates/umap/*.html"],
	css: [
		"node_modules/@gouvfr/dsfr/dist/dsfr.min.css",
		"node_modules/@gouvfr/dsfr/dist/utility/icons/icons.min.css",
	],
	safelist: [
		"body", // Useful to keep the Marianne font.
		"fr-modal--opened", // Useful for the responsive burger menu.
		"fr-responsive-img", // For blog posts.
		"fr-alert", // For blog posts.
		"fr-alert--info", // For blog posts.
		"fr-alert__title", // For blog posts.
		"fr-alert--sm", // For blog posts.
		"fr-link", // For blog posts.
		"fr-icon-arrow-right-line", // For blog posts.
		"fr-link--icon-right", // For blog posts.
	],
	output: "umap_dsfr/static/umap/dsfr-lite/",
};
