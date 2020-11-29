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
            <a class="nav-link"><router-link class='navbarTextColor' to="/study">
              Study</router-link></a>
            </li>
            <li class="nav-item">
            <a class="nav-link"><router-link class='navbarTextColor' to="/about">
              About</router-link></a>
            </li>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>

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