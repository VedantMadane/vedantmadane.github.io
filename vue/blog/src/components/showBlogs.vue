<template>
    <div v-theme="'wide'" id="show-blogs">
        <center><h2 >All Blog Articles</h2>
        <input type="text" v-model="search" placeholder="Filter"></center>
        <div class="single-blog" v-for="blog in filteredBlogs" :key="blog.id">
            <router-link v-bind:to="'/blog/'+blog.id"><h3 v-rainbow>{{blog.title | to-uppercase}}</h3></router-link>
            <article>
                {{blog.content | slice}} 
                <button @click="deletePost(blog.id)">Delete</button>
            </article>
        </div>
        {{ filteredBlogs }}
    </div>
</template>

<script>
// Imports
import searchMixin from '../mixins/searchMixin';
export default { 
    data () {
        return {
            blogs:[],
            search: ''
        }
            

    },
    methods: {
    deletePost(id){
        alert(this.blogs.length)
        for(let i = 0 ; i < this.blogs.length; i++) {
            if(this.blogs[i].id == id) {
                this.blogs.splice(i, 1)
            }
        }
        alert(this.blogs.length)
    }    
    },

    
    created(){
        this.$http.get('https://vue-blog-bd83c.firebaseio.com/posts.json').then(function(data){
            return data.json();
      
        }).then(function(data){
            var blogArray=[];
            for(let key in data)
            {
                //console.log(key+":"+data[key]);
                data[key].id=key;
                blogArray.push(data[key])
            }
            this.blogs=blogArray;
        })
    },
    computed:{
        
    }, 
    //Local Registered Filters
    filters:{
        'slice':function(value){
            return value.slice(0,100)+'...';
        }
    },
    mixins: [searchMixin]
}
</script>
<style>
#show-blogs{
    max-width: 800px;
    margin: 0 auto;

}
.single-blog{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eee;
}
a{
    text-decoration: none;
}
input[type="text"]{
    display: block;
    width: 500px;
    height: 30px;
    
}
</style>

