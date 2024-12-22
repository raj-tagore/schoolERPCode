<template>
<v-container>
    <v-row>
    <v-col 
    v-for="(classroom, index) in cards" 
    :key="index" 
    cols="6" 
    md="3" 
    lg="2" >
        <v-card>
        <v-img 
            :src="getRandomClassroomImage()" 
            aspect-ratio="16/9"
        ></v-img>
        <v-card-title>{{ classroom.title }}</v-card-title>
        <v-card-subtitle>{{ classroom.subtitle }}</v-card-subtitle>
        </v-card>
    </v-col>
    </v-row>
</v-container>
</template>

<script>



export default {
data() {
    return {
    cards: [
        { title: "Card 1", subtitle: "Subtitle 1" },
        { title: "Card 2", subtitle: "Subtitle 2" },
        { title: "Card 3", subtitle: "Subtitle 3" },
        { title: "Card 4", subtitle: "Subtitle 4" },
        { title: "Card 5", subtitle: "Subtitle 5" },
    ],
    images: [
        require('@/assets/classrooms/classroom1.jpg'),
        require('@/assets/classrooms/classroom2.jpg'),
        require('@/assets/classrooms/classroom3.jpg'),
        require('@/assets/classrooms/classroom4.jpg'),
    ],
    };
},
methods: {
    getRandomClassroomImage() {
        const index = Math.floor(Math.random() * this.images.length);
        return this.images[index];
    },
    async fetchClassrooms() {
        const response = await api.get()
    }
},
};
</script>
  