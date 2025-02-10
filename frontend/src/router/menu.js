import { useAuthStore } from "@/stores/auth"; // Pinia store

// Common filter for all routes
const defaultRouteFilter = (route) =>
    route.meta?.getDisplayName &&
    (route.meta?.permission
        ? useAuthStore().hasPermission(route.meta.permission)
        : true);

const currentRouteMeta = async (route) => {
    // All displayable routes which have a menu and matched the current route
    const routes = route.matched
        .filter(defaultRouteFilter)
        .filter((route) => route?.meta?.getMenu);

    const routeMeta = {};

    const app = routes.shift();

    const current = routes.pop();

    if (app?.meta) {
        // Populate the menu and display name
        const meta = app.meta;
        meta.menu = await app.meta.getMenu(route.params);
        meta.displayName = await app.meta.getDisplayName(route.params);
        routeMeta.app = meta;
    }

    if (current?.meta) {
        const meta = current.meta;
        meta.menu = await current.meta.getMenu(route.params);
        meta.displayName = await current.meta.getDisplayName(route.params);
        routeMeta.current = meta;
    }

    return routeMeta;
};

const getAppsMeta = async (route) =>
    // All displayable routes which are at top level
    Promise.all(
        route
            .filter(defaultRouteFilter)
            .filter((route) => !route.props)
            .map(async (route) => ({
                title: await route.meta.getDisplayName(),
                to: { name: route.meta.defaultRoute },
            })),
    );

export {
	defaultRouteFilter,
	currentRouteMeta,
	getAppsMeta,
}
