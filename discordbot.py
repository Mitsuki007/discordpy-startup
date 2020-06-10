from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


// Response for Uptime Robot
const http = require("http");
http
  .createServer(function(request, response) {
    response.writeHead(200, { "Content-Type": "text/plain" });
    response.end("Discord bot is active now \n");
  })
  .listen(3000);

// Discord bot implements
const discord = require("discord.js");
const client = new discord.Client();

client.on("ready", message => {
  console.log("bot is ready!");
  client.user.setPresence({
    game: { name: "まつエク", type: 1 }
  });
});

//スリープ
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

client.on("message", async message => {
  var user = message.member.nickname;
  if (!user) {
    user = message.author.username;
  }
  // if (message.author.id == "602037869476839435") {
  //   message.delete(100);
  //   return;
  // }
  //自分回避
  if (message.author.id === client.user.id) return;
  if (message.author.bot == true) return;

  if (message.content.match("おにぎり") && message.content.match("歌って")) {
    message.member.voiceChannel.join().then(connection => {
      const dispatcher = connection.playFile("assets/song01.mp3", {
        volume: 0.6
      });
      dispatcher.on("start", reason => {
        message.react("🔊");
        message.channel.send("🍝おにぎりのうた🍝");
      });
    });
    return;
  }

  if (message.content.match("マキちゃんただいま！")) {
    message.member.voiceChannel.join().then(connection => {
      const dispatcher = connection.playFile("assets/maki_welcome01.mp3", {
        volume: 1.5
      });
      dispatcher.on("start", reason => {
        message.react("🔊");
        message.channel.send("ヽ(ﾟ∀ﾟ)ﾉ!いらっしゃーい");
      });
    });
    return;
  }

  if (message.content.match("マキちゃんQ")) {
    message.member.voiceChannel.join().then(connection => {
      const dispatcher = connection.playFile("assets/maki_q01.mp3", {
        volume: 1.2
      });
      dispatcher.on("start", reason => {
        message.react("🔊");
        message.channel.send(":clapper:はじまりはじまりー( * ́ ́꒳`*)੭))");
      });
    });
    return;
  }
  
  if (message.content.match("マキちゃんおいでー！")) {
    message.member.voiceChannel.join().then(connection => {
      const dispatcher = connection.playFile("assets/maki_nandayo.mp3", {
        volume: 1.5
      });
      dispatcher.on("start", reason => {
        message.react("🔊");
        message.channel.send("なんだよー｜・_・)");
      });
    });
    return;
  }

  if (message.content.match("マキちゃんBGM")) {
    message.member.voiceChannel.join().then(connection => {
      const dispatcher = connection.playFile("assets/Love.mp3", {
        volume: 0.05
      });
      dispatcher.on("start", reason => {
        message.react("🔊");
        message.channel.send("やったれー！(o｀з’*)");
      });
    });
    return;
  }

  if (
    message.content.match("888") ||
    message.content.match("８８８") ||
    message.content.match("ぱちぱち")
  ) {
    let i = Math.floor(Math.random() * 10) + 1;
    if (i > 2) {
      return;
    }
    const eight = [
      "(≧∇≦*)最高だったー！！",
      "ლ(╹◡╹ლ)アゲアゲ～",
      "ଘ(੭ˊ꒳ˋ)੭✧尊いのぉ～",
      "(✿´꒳`)ﾉ°+.*すてきでしたー💕",
      "⁽⁽(ી₍₍⁽⁽(ી( ˆoˆ )ʃ)₎₎⁾⁾ʃ)₎₎感謝の踊りー",
      "ʕ灬￫ᴥ￩灬ʔぱちぱちー",
      "(人❛ᴗ❛)♪тнайк чоц♪",
      "(☝ ՞ਊ ՞)☝うぇーい！"
    ];
    const clap = eight[Math.floor(Math.random() * eight.length)];
    try {
      await message.channel.startTyping();
      await sleep(3800);
      await message.channel.send(clap);
      await message.channel.stopTyping();
    } catch {
      console.log("ぱちぱちエラー");
    }
    return;
  }
  const chat1 = "664061095329267733";
  const chat2 = "664061179970453515";
  const male = "672772801681424394";
  const female = "672772882790875136";
  const vc_01 = "664061127180681226";
  const vc_02 = "664061207631626242";
  const cate = "664060939687165955";

  //ランダム演出
  if (message.author.bot) {
    return;
  }
  if (message.member.user.bot == true) return;

  const serifu01 = [
    "おい( ・д・)ﾉ",
    "(。´・ω・)ん?",
    "なんだよー｜・_・)",
    "よっ( ´ ▽ ` )ﾉ",
    "このやろー٩(◦`꒳´◦)۶",
    "呼んだ？σ(ﾟ∀ﾟ)"
  ];

  const serifu01_resalut =
    serifu01[Math.floor(Math.random() * serifu01.length)];
  if (message.content.match("マキちゃーん")) {
    message.channel.send(serifu01_resalut);
  }

  if (message.author.bot) {
    return;
  }
  if (message.member.user.bot == true) return;

  const serifu02 = ["Hopeだよーん(^^♪", "今日はPeace!(。☌ᴗ☌｡):v::dove:"];

  const serifu02_resalut =
    serifu02[Math.floor(Math.random() * serifu02.length)];
  if (message.content.match("何吸ってるの？")) {
    message.channel.send(serifu02_resalut);
  }

  //固定返事
  if (message.content.match(/マキちゃん！！/)) {
    let channel = message.channel;
    let author = message.author.username;
    let reply_text = `なんだよー｜・_・)`;
    message
      .reply(reply_text)
      .then(message => console.log(`Sent message: ${reply_text}`))
      .catch(console.error);
    return;
  }

  if (message.content.match(/といれ！/)) {
    let channel = message.channel;
    let author = message.author.username;
    let reply_text = `いっといれ～٩(ˊᗜˋ*)و`;
    message
      .reply(reply_text)
      .then(message => console.log(`Sent message: ${reply_text}`))
      .catch(console.error);
    return;
  }

  if (message.content.match(/おはよ/)) {
    let channel = message.channel;
    let author = message.author.username;
    let reply_text = `よっ:two_hearts:`;
    message
      .reply(reply_text)
      .then(message => console.log(`Sent message: ${reply_text}`))
      .catch(console.error);
    return;
  }

  if (message.content.match(/おつかれさま/)) {
    let channel = message.channel;
    let author = message.author.username;
    let reply_text = `おつかれーヾ(－ω－○)oc`;
    message
      .reply(reply_text)
      .then(message => console.log(`Sent message: ${reply_text}`))
      .catch(console.error);
    return;
  }

  if (message.content.match(/おやすみー/)) {
    let channel = message.channel;
    let author = message.author.username;
    let reply_text = `暖かくして寝ろよなー( ́・ω・)`;
    message
      .reply(reply_text)
      .then(message => console.log(`Sent message: ${reply_text}`))
      .catch(console.error);
    return;
  }
});

client.on("voiceStateUpdate", async (newmember, oldmember) => {
  const mitsuki = await "360835671772102667";
  var ch_name = await "";
  const deiri = await "679375953721557016";
  const dlog = await "693140926402396201";
  var ch_name_mv = await "";
  console.dir(oldmember);
  if (newmember.user.id != mitsuki && oldmember.user.id != mitsuki) {
    if (oldmember.voiceChannel && !newmember.voiceChannel) {
      ch_name = await oldmember.voiceChannelID;
      await oldmember.guild.channels
        .get(deiri)
        .send(
          "✅おっす！" + oldmember.user.username + "さん！(<#" + ch_name + ">)"
        );
      await oldmember.guild.channels
        .get(dlog)
        .send("✅" + oldmember.user.username + "(<#" + ch_name + ">)");
    } else if (!oldmember.voiceChannel && newmember.voiceChannel) {
      ch_name = await newmember.voiceChannelID;

      await newmember.guild.channels
        .get(deiri)
        .send(
          "⛔" +
            newmember.user.username +
            "さんお疲れっすー。また来いよー(<#" +
            ch_name +
            ">)"
        );
      await newmember.guild.channels
        .get(dlog)
        .send("⛔" + newmember.user.username + "(<#" + ch_name + ">)");
    } else if (
      oldmember.voiceChannel &&
      newmember.voiceChannel &&
      oldmember.voiceChannel != newmember.voiceChannel
    ) {
      ch_name = await oldmember.voiceChannelID;
      ch_name_mv = await newmember.voiceChannelID;
      await newmember.guild.channels
        .get(deiri)
        .send(
          "□" +
            oldmember.user.username +
            "(<#" +
            ch_name_mv +
            ">) => (<#" +
            ch_name +
            ">)"
        );
      await newmember.guild.channels
        .get(dlog)
        .send(
          "□" +
            oldmember.user.username +
            "(<#" +
            ch_name_mv +
            ">) => (<#" +
            ch_name +
            ">)"
        );
    }
    return;
  }
});

if (process.env.DISCORD_BOT_TOKEN == undefined) {
  console.log("please set ENV: DISCORD_BOT_TOKEN");
  process.exit(0);
}

client.login(process.env.DISCORD_BOT_TOKEN);



@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
