<template>
  <div class="container">
    <!-- <div class="row">
      <div class="col-md-10"> -->

        <div class="card">
          <div class="card-body messages">

            <ul class="list-group">
              <li
                class="list-group-item"
                v-for="message in messages" :key="message.id"
              >
                <span class="user">
                  {{message.user}}:
                </span>
                <span>
                  {{message.body}}
                </span>
              </li>
            </ul>

          </div>
          <div class="card-footer bg-transparent">
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                placeholder=""
                aria-label="message input"
                v-on:keyup.13="submit"
                v-model="newMessage"
              >
              <div class="input-group-append">
                <button class="btn" type="button">
                  <i class="fas fa-angle-right"></i>
                </button>
              </div>
            </div>

          </div>
        </div>

      <!-- </div>
    </div> -->
  </div>
</template>

<script>

export default {
  name: 'messages',
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

  .container {
    height: 100%;
  }

  .card {
    height: 100%;
    background-color: #333;
  }

  .messages {
    height: 85%;
  }

  .message-input {
    background-color: #424242;
    bottom: 0px;
    margin-top: 10px;

  }

  .card-footer .input-group input.form-control {
    background-color: #424242;
    color: #aaa;
  }

  .user {
    font-weight: bold;
  }

  li.list-group-item {
    background-color: #424242;
    border: none;
    color: #aaa;
  }

  .btn {
    background-color: #bbb;
  }

  .user {
    color: #000;
  }

</style>
