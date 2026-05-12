require('dotenv').config();
const { Client, GatewayIntentBits, EmbedBuilder } = require('discord.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

const type = process.argv[2]; // 'commit' or 'branch'
const detail = process.argv[3]; // commit message or branch name
const author = process.argv[4] || 'System';

client.once('clientReady', async () => {
    const channelId = process.env.UPDATE_CHANNEL_ID;
    const channel = await client.channels.fetch(channelId);

    if (!channel) {
        console.error('Channel not found');
        process.exit(1);
    }

    const embed = new EmbedBuilder()
        .setColor(type === 'commit' ? 0x7289DA : 0xFFA500)
        .setAuthor({ name: author })
        .setTimestamp();

    if (type === 'commit') {
        embed.setTitle('🛠️ New Commit')
             .setDescription(`\`\`\`${detail}\`\`\``)
             .setFooter({ text: 'SLF.Mine Repository Update' });
    } else if (type === 'branch') {
        embed.setTitle('🌿 Branch Switched')
             .setDescription(`Now working on: **${detail}**`)
             .setFooter({ text: 'SLF.Mine Context Change' });
    }

    await channel.send({ embeds: [embed] });
    client.destroy();
});

client.login(process.env.DISCORD_TOKEN);
