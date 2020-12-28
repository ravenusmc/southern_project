<template>
  <div>
    <section>
      <div class="paragraph-div">
        <p>
          The goal of this project is really to fullfill a thought that I've had
          for a while now. That thought is the following: Can I use Sentiment
          analysis to further understand something from the time period that
          they were written in. Or, to put it another way, can sentiment
          analysis teach us something new about history that we don't know or to
          help confirm beliefs? If we had a lot of journals and letters written
          right before the Civil War would the Sentiment of those documents
          start to turn more and more negative? Thus, the purpose of this
          project is to start to see what can be learned from documents written
          from the early 19th to 20th centuries. Besides sentiment analysis,
          this project will also look at word counts and how they changed over
          time. Finally, there will be examing the sentiment of individual
          speeches. Thus slowly scroll down the page and see what my study has
          found...
        </p>
      </div>

      <div class="pic-div"></div>
    </section>

    <!-- Start of Graph Section  -->
    <section id='graph-area'>
      <GraphCard
        :typeOne="typeOne"
        :data="sentimentOverTime"
        :options="chartOptionsOne"
      >
      </GraphCard>

      <Form/>

    </section>
    <!-- End of Graph Section  -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import GraphCard from "@/components/graphs/GraphCard.vue";
import Form from "@/components/study/Form.vue";

export default {
  name: "Explanation",
  components: {
    GraphCard,
    Form,
  },
  data() {
    return {
      typeOne: "LineChart",
      chartOptionsOne: {
        title: "Sentiment of all Texts Over Time",
        legend: { position: "top" },
        colors: ["#333"],
        height: 600,
        width: 1200,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          viewWindow: {
            min: -0.025,
          },
        },
      },
    };
  },
  computed: {
    ...mapGetters(["sentimentOverTime"]),
  }, // End Computed properties
};
</script>

<style scoped>
section {
  margin: 50px 100px 50px 100px;
  margin-top: 50px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

.paragraph-div {
  font-size: 20px;
  width: 80%;
  text-align: left;
}

.pic-div {
  background-image: url("../../assets/images/letters.jpg");
  height: 500px;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  color: white;
}

#graph-area {
  display: flex;
  flex-direction: column;
}

@media only all and (max-width: 1000px) {
  section {
    margin: 50px 100px 50px 100px;
    margin-top: 50px;
    display: grid;
    grid-template-columns: 1fr;
  }

  .paragraph-div {
    width: 100%;
  }

  .pic-div {
    display: none;
  }
}
</style>