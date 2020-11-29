<template>
  <div>
    <Navbar />
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/view/Navbar.vue";
import Footer from "@/components/view/Footer.vue";

export default {
  name: "Study",
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style scoped>
</style>