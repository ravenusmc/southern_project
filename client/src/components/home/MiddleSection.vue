<template>
  <div>
    <section>
      <div class="div-one common-div-features">One</div>

      <div class="div-two common-div-features">The Study</div>

      <div class="div-three common-div-features">three</div>
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
  border: 2px solid red;
  height: 600px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.common-div-features {
	margin: 0 3% 0 3%;
  height: 50%;
  width: 50%;
}

.div-one {
  border: 2px solid blue;
}

.div-two {
  border: 2px solid blue;
	border-radius: 100%;
}
</style>