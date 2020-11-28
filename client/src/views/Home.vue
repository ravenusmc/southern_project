<template>
  <div>
    <Navbar />
    <div class="header">
      <b-jumbotron
        class="header"
        header="Southern Project"
        lead="Understanding the South through Literature and NLP"
      >
      </b-jumbotron>
    </div>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/view/Navbar.vue";
import Footer from "@/components/view/Footer.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style scoped>
.header {
  background-image: url("../assets/images/jumbotron.jpg");
  height: 400px;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  color: white;
}
</style>
