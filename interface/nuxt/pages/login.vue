<template>
  <v-container>
    <v-card class="login-card" elevation="10">
      <v-form ref="form" @submit.prevent="login">
        <v-card-title>
          <div class="text-md-center pa-5">ログイン</div>
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field
                v-model="email"
                :rules="rules.email"
                label="メールアドレス"
                type="email"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field
                v-model="password"
                :rules="rules.password"
                label="パスワード"
                type="password"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn type="submit" block color="primary" height="40"> ログイン </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-form>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
const form = ref()
const email = ref('')
const password = ref('')

const rules = {
  email: [
    (value: string) => {
      if (value) return true
      return 'メールアドレスを入力してください'
    }
  ],
  password: [
    (value: string) => {
      if (value) return true
      return 'パスワードを入力してください'
    }
  ]
}

const login = async () => {
  const { valid } = await form.value.validate()
  if (!valid) return

  const response = await useApi('login', {
    method: 'POST',
    body: {
      email: email.value,
      password: password.value
    }
  })

  console.log(response.error.value?.response?.status)

  console.log(response)
}
</script>

<style scoped lang="scss">
.login-card {
  max-width: 480px;
  margin: 20vh auto 0 auto;
}
</style>
