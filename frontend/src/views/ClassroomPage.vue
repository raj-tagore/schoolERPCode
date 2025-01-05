<template>
<v-container>
    Classroom ID: {{ id }}
</v-container>
</template>

<script>
import { onMounted } from 'vue';
import api from '@/services/api';

export default {
    props: ['id'],
    setup(props) {
        onMounted(() => {

        });
    }
}
</script>