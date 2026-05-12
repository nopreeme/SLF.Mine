const { SlashCommandBuilder, EmbedBuilder, PermissionFlagsBits } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('devupdate')
        .setDescription('Post a development update')
        .addStringOption(option =>
            option.setName('title')
                .setDescription('The title of the update')
                .setRequired(true))
        .addStringOption(option =>
            option.setName('content')
                .setDescription('The content of the update')
                .setRequired(true))
        .setDefaultMemberPermissions(PermissionFlagsBits.Administrator),
    async execute(interaction) {
        const title = interaction.options.getString('title');
        const content = interaction.options.getString('content');

        const embed = new EmbedBuilder()
            .setColor(0x00AE86)
            .setTitle(title)
            .setAuthor({ name: 'SLF.Mine Development Team' })
            .setDescription(content)
            .setTimestamp()
            .setFooter({ text: 'SLF.Mine Progress Report' });

        await interaction.channel.send({ embeds: [embed] });
        await interaction.reply({ content: 'Development update has been posted successfully!', ephemeral: true });
    },
};
