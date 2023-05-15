<script setup lang="ts">
const emailAddress = ref("");
const password = ref("");

const login = () => {
  console.log(emailAddress, password)
}
</script>

<template>
  <div>
    <v-text-field v-model="emailAddress" label="メールアドレス" />
    <v-text-field v-model="password" label="パスワード" />
    <v-btn @click="login()">ログイン</v-btn>
  </div>
</template>
