<template>
  <div>
    <section>
      <div class="div-one common-div-features"></div>

      <div class="div-two common-div-features">The Study</div>

      <div class="div-three common-div-features"></div>
    </section>
  </div>
</template>

<script>
export default {
  name: "MiddleSection",
};
</script>

<style scoped>
section {
  height: 600px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 50px;
}

.common-div-features {
  margin: 0 3% 0 3%;
  height: 80%;
  width: 50%;
}

.div-one {
  background-image: url("../../assets/images/black_white.jpg");
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

.div-two {
  height: 10%;
  width: 10%;
  border-radius: 100%;
}

.div-three {
  background-image: url("../../assets/images/lit_pic.jpg");
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

@media only all and (max-width: 900px) {
  section {
    flex-direction: column;
  }
}
</style>