import discord, jishaku, discord.ui
from discord.ext import commands
from discord import ui, app_commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=",", intents = intents)

@bot.event
async def on_ready():
  await bot.tree.sync()
  await bot.load_extension("jishaku")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="riel"))
  print ("bot is online")

@bot.command()
async def ping(ctx):
  await ctx.send(f"pong ``{round(bot.latency * 1000)}ms``")

class pronounRoles(discord.ui.View):
  @discord.ui.button(label="he/him", style=discord.ButtonStyle.grey, custom_id="him")
  async def him(self, interaction: discord.Interaction, button):
    he = discord.utils.get(interaction.guild.roles, name="him")
    if he in interaction.user.roles:
      await interaction.user.remove_roles(he)
      await interaction.response.send_message(f"removed {he} role", ephemeral=True)
    else:
      await interaction.user.add_roles(he)
      await interaction.response.send_message(f"added {he} role", ephemeral=True)
  @discord.ui.button(label="she/her", style=discord.ButtonStyle.grey, custom_id="she")
  async def her(self, interaction: discord.Interaction, button):
    she = discord.utils.get(interaction.guild.roles, name="she")
    if she in interaction.user.roles:
      await interaction.user.remove_roles(she)
      await interaction.response.send_message(f"removed {she} role", ephemeral=True)
    else:
      await interaction.user.add_roles(she)
      await interaction.response.send_message(f"added {she} role", ephemeral=True)
  @discord.ui.button(label="they/them", style=discord.ButtonStyle.grey, custom_id="they")
  async def they(self, interaction: discord.Interaction, button):
    they = discord.utils.get(interaction.guild.roles, name="they")
    if they in interaction.user.roles:
      await interaction.user.remove_roles(they)
      await interaction.response.send_message(f"removed {they} role", ephemeral=True)
    else:
      await interaction.user.add_roles(they)
      await interaction.response.send_message(f"added {they} role", ephemeral=True)
  @discord.ui.button(label="any", style=discord.ButtonStyle.gray, custom_id="any")
  async def any(self, interaction: discord.Interaction, button):
    any = discord.utils.get(interaction.guild.roles, name="any")
    if any in interaction.user.roles:
      await interaction.user.remove_roles(any)
      await interaction.response.send_message(f"removed {any} role", ephemeral=True)
    else:
      await interaction.user.add_roles(any)
      await interaction.response.send_message(f"added {any} role", ephemeral=True)

class programRoles(discord.ui.View):
  @discord.ui.button(label="videostar", style=discord.ButtonStyle.grey, custom_id="vs")
  async def vs(self, interaction: discord.Interaction, button):
    vs = discord.utils.get(interaction.guild.roles, name="video star")
    if vs in interaction.user.roles:
      await interaction.user.remove_roles(vs)
      await interaction.response.send_message(f"removed {vs} role", ephemeral=True)
    else:
      await interaction.user.add_roles(vs)
      await interaction.response.send_message(f"added {vs} role", ephemeral=True)
  @discord.ui.button(label="after effects", style=discord.ButtonStyle.grey, custom_id="ae")
  async def ae(self, interaction: discord.Interaction, button):
    ae = discord.utils.get(interaction.guild.roles, name="after effects")
    if ae in interaction.user.roles:
      await interaction.user.remove_roles(ae)
      await interaction.response.send_message(f"removed {ae} role", ephemeral=True)
    else:
      await interaction.user.add_roles(ae)
      await interaction.response.send_message(f"added {ae} role", ephemeral=True)
  @discord.ui.button(label="alight motion", style=discord.ButtonStyle.grey, custom_id="am")
  async def am(self, interaction: discord.Interaction, button):
    am = discord.utils.get(interaction.guild.roles, name="alight motion")
    if am in interaction.user.roles:
      await interaction.user.remove_roles(am)
      await interaction.response.send_message(f"removed {am} role", ephemeral=True)
    else:
      await interaction.user.add_roles(am)
      await interaction.response.send_message(f"added {am} role", ephemeral=True)

class funRoles(discord.ui.View):
  @discord.ui.button(label="dt", style=discord.ButtonStyle.grey, custom_id="dt")
  async def dt(self, interaction: discord.Interaction, button):
    dt = discord.utils.get(interaction.guild.roles, name="dt")
    if dt in interaction.user.roles:
      await interaction.user.remove_roles(dt)
      await interaction.response.send_message(f"removed {dt} role", ephemeral=True)
    else:
      await interaction.user.add_roles(dt)
      await interaction.response.send_message(f"added {dt} role", ephemeral=True)
  @discord.ui.button(label="ops", style=discord.ButtonStyle.grey, custom_id="ops")
  async def ops(self, interaction: discord.Interaction, button):
    ops = discord.utils.get(interaction.guild.roles, name="ops")
    if ops in interaction.user.roles:
      await interaction.user.remove_roles(ops)
      await interaction.response.send_message(f"removed {ops} role", ephemeral=True)
    else:
      await interaction.user.add_roles(ops)
      await interaction.response.send_message(f"added {ops} role", ephemeral=True)
  @discord.ui.button(label="help", style=discord.ButtonStyle.grey, custom_id="help")
  async def help(self, interaction: discord.Interaction, button):
    help = discord.utils.get(interaction.guild.roles, name="help")
    if help in interaction.user.roles:
      await interaction.user.remove_roles(help)
      await interaction.response.send_message(f"removed {help} role", ephemeral=True)
    else:
      await interaction.user.add_roles(help)
      await interaction.response.send_message(f"added {help} role", ephemeral=True)
  @discord.ui.button(label="collab", style=discord.ButtonStyle.grey, custom_id="mep")
  async def mep(self, interaction: discord.Interaction, button):
    collab = discord.utils.get(interaction.guild.roles, name="collab")
    if collab in interaction.user.roles:
      await interaction.user.remove_roles(collab)
      await interaction.response.send_message(f"removed {collab} role", ephemeral=True)
    else:
      await interaction.user.add_roles(collab)
      await interaction.response.send_message(f"added {collab} role", ephemeral=True)
  @discord.ui.button(label="hotping", style=discord.ButtonStyle.grey, custom_id="hotping")
  async def hotping(self, interaction: discord.Interaction, button):
    hotping = discord.utils.get(interaction.guild.roles, name="hotping")
    if hotping in interaction.user.roles:
      await interaction.user.remove_roles(hotping)
      await interaction.response.send_message(f"removed {hotping} role", ephemeral=True)
    else:
      await interaction.user.add_roles(hotping)
      await interaction.response.send_message(f"added {hotping} role", ephemeral=True)
  @discord.ui.button(label="vc", style=discord.ButtonStyle.grey, custom_id="vc")
  async def vc(self, interaction: discord.Interaction, button):
    vc = discord.utils.get(interaction.guild.roles, name="vc")
    if vc in interaction.user.roles:
      await interaction.user.remove_roles(vc)
      await interaction.response.send_message(f"removed {vc} role", ephemeral=True)
    else:
      await interaction.user.add_roles(vc)
      await interaction.response.send_message(f"added {vc} role", ephemeral=True)






@bot.command()
async def test(ctx):
  embed = discord.Embed(description="choose the roles that best fit you!", color=discord.Colour.dark_embed())
  embed.set_image(url="https://cdn.discordapp.com/attachments/1224504052340232223/1232582625894600735/56ce61caf01f876af23e8eae39a85b0d.jpg?ex=6629fb86&is=6628aa06&hm=237bae985a93e1d3af87345404cb1a871dec479336046a69964115f9f92ae75c&")

  embed2 = discord.Embed(color=discord.Colour.dark_embed())
  embed2.set_footer(text="misc roles")

  embed3 = discord.Embed(color=discord.Colour.dark_embed())
  embed3.set_footer(text="program roles")

  embed4 = discord.Embed(color=discord.Colour.dark_embed())
  embed4.set_footer(text="pronoun roles")

  await ctx.send(embed=embed)
  await ctx.send(embed=embed2, view=funRoles())
  await ctx.send(embed=embed3, view=programRoles())
  await ctx.send(embed=embed4, view=pronounRoles())

@bot.command()
async def boost(ctx):
  embed = discord.Embed(title="akemi booster perks!", description="**boost us and get...**\n\ncare6ul shake pack 1\nexclusive project files and presets from <@1090735477914603600>\na free edit\n& more! (whanever i come up with them)", color=discord.Color.dark_embed())
  embed.set_image(url="https://cdn.discordapp.com/attachments/1224504052340232223/1229260595694534666/guitar-shredding-scott-pilgrim.gif?ex=662f0924&is=661c9424&hm=81b8a263f9d497f8d7c6c53481e4998146c17e2bc4e7541cc7f04d30d4e34d24&")
  await ctx.send(embed=embed)

@bot.command(aliases=["close", "lock"])
@commands.has_permissions(administrator=True)
async def lockdown(ctx):
    embed = discord.Embed(description=f"> :lock: {ctx.author.mention}: locked down {ctx.channel.mention}.", color=discord.Color.yellow())
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["open"])
@commands.has_permissions(administrator=True)
async def unlock(ctx):
    embed = discord.Embed(description=f"> :unlock: {ctx.author.mention}: unlocked {ctx.channel.mention}.", color=discord.Color.yellow())
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(embed=embed)

class testModal(discord.ui.Modal, title="akemi application"):
  username = ui.TextInput(label="what is your instagram username",
                          placeholder="care6ul",
                          style=discord.TextStyle.short)
  link = ui.TextInput(label="link to your edit",
                      placeholder="streamable and instagram only!",
                      style=discord.TextStyle.short)

  async def on_submit(self, interaction: discord.Interaction):
    embed = discord.Embed(
        title="new application!",
        description=
        f"**application from:**\n{interaction.user.mention}\n **ig username:** \n {self.username.value}\n **link:**\n {self.link}",
        color=discord.Color.light_embed())
    embed.set_thumbnail(url=interaction.user.avatar)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="apply")
async def apply(interaction: discord.Interaction):
  await interaction.response.send_modal(testModal())


@bot.tree.command(name="accept")
@app_commands.checks.has_permissions(administrator=True)
async def accept(interaction: discord.Interaction, user: discord.User):
  try:
    dm_channel = await user.create_dm()
    embed = discord.Embed(
        title="you've been accepted into akemi!",
        description=
        "send a screenshot of this message into <#1211741086683373618>, and a staff member will change your role in the server!",
        color=discord.Color.light_embed())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/1095576214342742016/1211748869378019449/ACCEPT.png?ex=65ef5413&is=65dcdf13&hm=53bf6a243112ad6341f62fe4fa7ba771f5229afa4fca02fcf3921e981f51e9dd&"
    )
    await dm_channel.send(embed=embed)
    await interaction.response.send_message(f"accepted {user.mention}!",
                                            ephemeral=True)
  except discord.HTTPException as e:
    await interaction.response.send_message(f"Error: {e}", ephemeral=True)


@bot.tree.command(name="reapp")
@app_commands.checks.has_permissions(administrator=True)
async def reapp(interaction: discord.Interaction, user: discord.User,
                message: str):
  try:
    dm_channel = await user.create_dm()
    embed = discord.Embed(
        title="you've been reapped from akemi.",
        description=
        f"here is the feedback that your reviewer sent, \n > ``{message}``",
        color=discord.Color.light_embed())
    embed.set_footer(text="you can reapp in 24 hours")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/1095576214342742016/1211739972051406888/REAPP.png?ex=65ef4bca&is=65dcd6ca&hm=ff4df475785ee67dd5da7722cc7c3780c9056b3bd19561c7ce06a4d1f1d47092&"
    )
    await dm_channel.send(embed=embed)
    await interaction.response.send_message(f"reapped {user.mention}!",
                                            ephemeral=True)
  except discord.HTTPException as e:
    await interaction.response.send_message(f"Error: {e}", ephemeral=True)





bot.run("MTE0NjU5NDczNjU1MjAxODA4Mw.Gw5Rrb.afOVZTLOSJZUbmbxkDkTsJIopx58pWwYp69zZ0")