<template>
  <div>
    <!-- Bootstrap From  -->
    <form @submit="submitForm">
      <div class="form-group">
        <label><span>Select Decade:</span></label>
        <select class="custom-select" v-model="decade" name="speech">
          <option v-for="decade in decades" v-bind:key="decade" :value="decade">
            {{ decade }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-outline-dark">Submit</button>
    </form>
    <!-- End Boostrap Form -->
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "Form",
  data() {
    return {
      decade: "1790-1800",
      value: this.initalValue,
      decades: [
        "1790-1800",
        "1801-1810",
        "1811-1820",
        "1821-1830",
        "1831-1840",
        "1841-1850",
        "1851-1860",
        "1861-1870",
        "1871-1880",
        "1881-1890",
        "1891-1900",
        "1901-1910",
        "1911-1920",
        "1921-1930",
      ],
    };
	},
	methods: {
    ...mapActions([
      'fetchWordsByDecade',
    ]),
		submitForm(evt) {
			evt.preventDefault();
      const payload = {
        decade: this.decade,
      };
      this.fetchWordsByDecade({ payload });
		},
	},
};
</script>

<style scoped>
</style>