import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    sentimentOverTime: [
      ['Year', 'Sentiment'],
      [1709, 0.13],
      [1732, 0.11],
      [1788, 0.04],
      [1791, 0.12],
      [1798, 0.09],
      [1800, -0.01],
      [1817, 0.1],
      [1829, 0.12],
      [1832, 0.09921721253025265],
      [1834, 0.08],
      [1835, 0.0731763942998558],
      [1837, 0.1],
      [1840, 0.07328505563947857],
      [1841, 0.12],
      [1844, 0.08],
      [1845, 0.07332462326360184],
      [1849, 0.06],
      [1852, 0.07958517547371646],
      [1853, 0.08852451916550493],
      [1854, 0.09052173276728169],
      [1855, 0.08],
      [1857, 0.1505064949032346],
      [1858, 0.05],
      [1860, 0.07920515348822518],
      [1862, 0.08],
      [1864, 0.09437847093614979],
      [1867, 0.05639661338358422],
      [1872, 0.09],
      [1874, 0.09],
      [1875, 0.06],
      [1879, 0.08],
      [1880, 0.06911441888495899],
      [1881, 0.03],
      [1882, 0.07],
      [1883, 0.05621670137102116],
      [1884, 0.08],
      [1885, 0.046223301353220385],
      [1887, 0.06101734207946444],
      [1888, 0.05],
      [1891, 0.08],
      [1892, 0.096494759221633],
      [1894, 0.06703106354027465],
      [1895, 0.05],
      [1896, 0.03],
      [1897, 0.07708783926181927],
      [1898, 0.07],
      [1899, 0.08221777730845425],
      [1900, 0.07181251693736002],
      [1901, 0.08151403426449656],
      [1902, 0.06672093053530621],
      [1904, 0.05464778920364917],
      [1905, 0.07147646542910839],
      [1907, 0.05846966313964699],
      [1910, 0.08],
      [1913, 0.06648607180798183],
      [1914, 0.05],
      [1917, 0.07],
      [1919, 0.06923144174066485],
      [1920, 0.11],
      [1922, 0.02],
      [1927, 0.09]
    ],
    wordAndCountData: [],
  },

  getters: {
    sentimentOverTime: (state) => state.sentimentOverTime,
  },

  actions: {

    fetchWordsByDecade: ({ commit }, { payload }) => {
      const path = 'http://localhost:5000/fetch_words_by_decade';
        axios.post(path, payload)
        .then((res) => {
          console.log(res.data)
          commit('setWordAndCountData', payload);
        });
    },

  },

  mutations: {

    setWordAndCountData(state, data) {
      state.wordAndCountData = data;
    },

  },

})
