<template>
  <div>
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Southern Project</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <li class="nav-item active">
              <a class="nav-link"><router-link class="navbarTextColor" to="/">
              Home
              </router-link></a>
            </li>
            <li class="nav-item">
            <a class="nav-link"><router-link class='navbarTextColor' to="/about">
              About</router-link></a>
            </li>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>

    <!-- <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand"><router-link class='navbarTextColor' to="/">Southern Project
        </router-link></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse"
      data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
      aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link"><router-link class='navbarTextColor' to="/">Home
            </router-link></a>
          </li>
          <li class="nav-item">
            <a class="nav-link"><router-link class='navbarTextColor' to="/about">
              About</router-link></a>
          </li>
        </ul>
      </div>
    </nav> -->
  </div>
</template>

<style>
.navbarTextColor {
  color: white;
}
.navbarTextColor:hover {
  color: red;
}
</style>