import classroomsRoutes from "@/apps/classrooms/routes";
import subjectsRoutes from "@/apps/subjects/routes"
import usersRoutes from "@/apps/users/routes"
import announcementsRoutes from "@/apps/announcements/routes"
import assignmentsRoutes from "@/apps/assignments/routes"

export default [
    ...classroomsRoutes,
    ...subjectsRoutes,
    ...usersRoutes,
    ...announcementsRoutes,
    ...assignmentsRoutes,
];
