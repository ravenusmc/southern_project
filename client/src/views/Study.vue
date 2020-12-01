<template>
  <div>
    <Navbar />
    <Explanation />
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/view/Navbar.vue";
import Explanation from "@/components/study/Explanation.vue";
import Footer from "@/components/view/Footer.vue";

export default {
  name: "Study",
  components: {
    Navbar,
    Explanation,
    Footer,
  },
};
</script>

<style scoped>
</style>