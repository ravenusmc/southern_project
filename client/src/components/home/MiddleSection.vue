<template>
  <div>
    <section>
      <div class="div-one common-div-features"></div>

      <div class="div-two">
        <a class="nav-link"
          ><router-link to="/study" class="study-button"
            >The Study</router-link
          ></a
        >
      </div>

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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 10%;
  width: 10%;
  border-radius: 100%;
  border: 2px solid black;
  padding: 50px;
  background-color: #15a3b8;
}

.study-button {
  color: white;
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
    height: 1000px;
  }

  .common-div-features {
    height: 600px;
    width: 400px;
  }

  .div-two {
    padding: 80px;
    margin: 15px 0px 15px 0px;
  }
  
}
</style>