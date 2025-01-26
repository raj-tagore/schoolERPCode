<template>
    <v-card variant="flat">
        <v-text-field
        v-model="searchQuery"
        label="Click here to search by name"
        @input="fetchAccounts"
        outlined
        density="comfortable"
        ></v-text-field>
        <v-container>
        <v-row>
          <v-col cols="12" md="3" v-if="teacherResults.length > 0">
            <v-card>
              <v-card-title>Staff</v-card-title>
              <v-list lines="two">
                <v-list-item
                  v-for="item in teacherResults.slice(0, 10)"
                  :key="item.id"
                  :title="item.user.full_name"
                  :subtitle="item.identifier"
                  class="ma-1 border"
                  density="compact"
                >
                  <template v-slot:append>
                    <v-btn
                      icon="mdi-arrow-right"
                      size="x-small"
                      variant="outlined"
                      @click="viewAccount(item)"
                    ></v-btn>
                  </template>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <v-col cols="12" md="3" v-if="studentResults.length > 0">
            <v-card>
              <v-card-title>Students</v-card-title>
              <v-list lines="two">
                <v-list-item
                  v-for="item in studentResults.slice(0, 10)"
                  :key="item.id"
                  :title="item.user.full_name"
                  :subtitle="'ID: ' + item.id"
                  class="ma-1 border"
                  density="compact"
                >
                  <template v-slot:append>
                    <v-btn
                      icon="mdi-arrow-right"
                      size="x-small"
                      variant="outlined"
                      @click="viewAccount(item)"
                    ></v-btn>
                  </template>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <v-col cols="12" md="3" v-if="parentResults.length > 0">
            <v-card>
              <v-card-title>Parents</v-card-title>
              <v-list lines="two">
                <v-list-item
                  v-for="item in parentResults.slice(0, 10)"
                  :key="item.id"
                  :title="item.user.full_name"
                  :subtitle="'ID: ' + item.id"
                  class="ma-1 border"
                  density="compact"
                >
                  <template v-slot:append>
                    <v-btn
                      icon="mdi-arrow-right"
                      size="x-small"
                      variant="outlined"
                      @click="viewAccount(item)"
                    ></v-btn>
                  </template>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
        </v-container>
    </v-card>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { getTeachers, getStudents, getParents } from "@/apps/users/api";
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const searchQuery = ref("");
  const teacherResults = ref([]);
  const studentResults = ref([]);
  const parentResults = ref([]);
  
  const fetchAccounts = async () => {
    if (!searchQuery.value) {
      teacherResults.value = [];
      studentResults.value = [];
      parentResults.value = [];
      return;
    }
  
    try {
      const filter = { name: searchQuery.value };
      
      const [teachers, students, parents] = await Promise.all([
        getTeachers(filter),
        getStudents(filter),
        getParents(filter)
      ]);

      teacherResults.value = teachers;
      studentResults.value = students;
      parentResults.value = parents;
    } catch (error) {
      console.error("Error fetching accounts:", error);
    }
  };

  const viewAccount = (item) => {
    if (studentResults.value.includes(item)) {
      router.push({ name: 'Student', params: { studentId: item.id }});
    }
    // TODO: Add routing for teachers and parents when those routes are created
  };
  </script>
  