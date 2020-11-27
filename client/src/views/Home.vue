<template>
  <div>
    <Navbar />
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
