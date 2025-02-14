import classroomsRoutes from "@/apps/classrooms/routes";
import subjectsRoutes from "@/apps/subjects/routes"
import studentsRoutes from "@/apps/students/routes"
import parentsRoutes from "@/apps/parents/routes"
import teachersRoutes from "@/apps/teachers/routes"
import announcementsRoutes from "@/apps/announcements/routes"
import assignmentsRoutes from "@/apps/assignments/routes"
import attachmentRoutes from "@/apps/attachments/routes"
import financesRoutes from "@/apps/finances/routes"
import calendarRoutes from "@/apps/events/routes"

export default [
    ...classroomsRoutes,
    ...subjectsRoutes,
	...studentsRoutes,
	...parentsRoutes,
	...teachersRoutes,
    ...announcementsRoutes,
    ...assignmentsRoutes,
    ...attachmentRoutes,
    ...financesRoutes,
    ...calendarRoutes,
];
