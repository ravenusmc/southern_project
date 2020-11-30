<template>
  <div>
    <Navbar />
    <div class="container">
      <b-jumbotron
        class="header"
        header="The Southern Project"
        lead="Understanding the South through Literature and Sentiment Analysis"
      >
      </b-jumbotron>
    </div>
    <MiddleSection />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/view/Navbar.vue";
import MiddleSection from "@/components/home/MiddleSection.vue";
import Footer from "@/components/view/Footer.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    MiddleSection,
    Footer,
  },
};
</script>

<style scoped>
.header {
  background-image: url("../assets/images/jumbotron.jpg");
  height: 500px;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  color: white;
}
</style>
