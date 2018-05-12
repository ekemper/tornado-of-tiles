<template>
<div>

  <div class="container">
    <div class="row">
      <div class="col-md-10 messages">
        <div v-for="message in messages" :key="message.id">
          <span>
            {{message.user}}
          </span>
          <span>
            {{message.body}}
          </span>
        </div>

      </div>
    </div>

    <div class="row message-input">
      <div class="col-sm">

        <div class="input-group mb-3">
          <input
            type="text"
            class="form-control"
            placeholder=""
            aria-label="message input"
            v-on:keyup.13="submit"
            v-model="newMessage"
          >
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button">
              <i class="fas fa-angle-right"></i>
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>

</div>
</template>

<script>

export default {
  name: 'main',
  data () {
    return {
      messages: [
        {
          user: 'this dude',
          body: 'booboo',
          id: 1
        },
        {
          user: 'dinosaur',
          body: 'eat meat!',
          id: 2
        }
      ],
      currentUser: 'me',
      newMessage: ''
    }
  },
  methods: {
    submit
  }
}

function submit () {
  this.messages.push({
    user: this.currentUser,
    body: this.newMessage
  })

  this.newMessage = ''
}

</script>

<style>
  .message-input {
    bottom: 0px;
  }
</style>
