<template>
    <div class="grid grid-cols-4 gap-4">
        <div v-for="i in cardData" :key="i.title">
            <Card
                :title="i.title"
                :content="i.content"
                :text="i.text"
            />
        </div>
    </div>
</template>

<script>
import Card from '../components/Card.vue'

export default {
    data(){
        return {
            cardData: [
                {
                    title: 'AAA',
                    content: 'fuck me',
                    text: 'I love you'
                },
                {
                    title: 'BBB',
                    content: 'fuck you',
                    text: 'fuck'
                },
                {
                    title: 'CCC',
                    content: 'eat my shit',
                    text: 'Hi'
                },
                {
                    title: 'DDD',
                    content: 'suck my dick',
                    text: 'Hi'
                },
                {
                    title: 'DDD',
                    content: 'suck my dick',
                    text: 'Hi'
                },
                {
                    title: 'DDD',
                    content: 'suck my dick',
                    text: 'Hi'
                },
                {
                    title: 'DDD',
                    content: 'suck my dick',
                    text: 'Hi'
                },
                {
                    title: 'DDD',
                    content: 'suck my dick',
                    text: 'Hi'
                }
            ]
        }
    },
    components: {
        Card
    }
}
</script>