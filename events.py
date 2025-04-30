def get_events(default_player):
    return [
        # 1. Evil Creeper (Fixed command formatting)
        {
            "name": "Evil Creeper",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:creeper ~ ~ ~", "delay": 0},
                {"cmd": "playsound random.fuse @a", "delay": 1},
                {"cmd": f"effect {default_player} mining_fatigue 5 1 true", "delay": 2}
            ]
        },

        # 2. Thunder Storm
        {
            "name": "Thunder Storm",
            "duration": 20,
            "commands": [
                {"cmd": "weather thunder", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:lightning_bolt ~ ~ ~", "delay": 2},
                {"cmd": "playsound ambient.weather.thunder @a", "delay": 0}
            ]
        },

        # 3. Chaos Mode
        {
            "name": "Chaos Mode",
            "duration": 30,
            "commands": [
                {"cmd": f"effect {default_player} blindness 5 1 true", "delay": 0},
                {"cmd": f"execute as {default_player} run effect {default_player} levitation 3 1 true", "delay": 2},
                {"cmd": f"execute as {default_player} run summon minecraft:lightning_bolt ~ ~ ~", "delay": 4},
                {"cmd": "playsound mob.enderdragon.growl @a", "delay": 1}
            ]
        },

        # 4. Monster Party
        {
            "name": "Monster Party",
            "duration": 45,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:zombie ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:skeleton ~ ~ ~", "delay": 2},
                {"cmd": "playsound mob.zombie.say @a", "delay": 1},
                {"cmd": f"effect {default_player} darkness 10 1 true", "delay": 3}
            ]
        },

        # 5. Bouncy Castle
        {
            "name": "Bouncy Castle",
            "duration": 15,
            "commands": [
                {"cmd": f"effect {default_player} jump_boost 15 8 true", "delay": 0},
                {"cmd": f"effect {default_player} speed 15 3 true", "delay": 0},
                {"cmd": "playsound random.levelup @a", "delay": 1}
            ]
        },

        # 6. Confusion Rain
        {
            "name": "Confusion Rain",
            "duration": 25,
            "commands": [
                {"cmd": "weather rain", "delay": 0},
                {"cmd": f"effect {default_player} nausea 10 1 true", "delay": 2},
                {"cmd": f"effect {default_player} slowness 10 2 true", "delay": 4},
                {"cmd": "playsound ambient.weather.rain @a", "delay": 0}
            ]
        },

        # 7. Fireworks Show
        {
            "name": "Fireworks Show",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:firework_rocket ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:firework_rocket ~ ~ ~5", "delay": 2},
                {"cmd": f"execute as {default_player} run summon minecraft:firework_rocket ~ ~ ~-5", "delay": 4},
                {"cmd": "playsound firework.launch @a", "delay": 0}
            ]
        },

        # 8. Random Teleport
        {
            "name": "Random Teleport",
            "duration": 10,
            "commands": [
                {"cmd": "spreadplayers ~ ~ 10 20 @a", "delay": 0},
                {"cmd": "playsound mob.endermen.portal @a", "delay": 0},
                {"cmd": f"effect {default_player} blindness 3 1 true", "delay": 0}
            ]
        },

        # 9. Speed Demon
        {
            "name": "Speed Demon",
            "duration": 15,
            "commands": [
                {"cmd": f"effect {default_player} speed 15 10 true", "delay": 0},
                {"cmd": f"effect {default_player} jump_boost 15 5 true", "delay": 0},
                {"cmd": "playsound random.levelup @a", "delay": 1}
            ]
        },

        # 10. Treasure Hunt
        {
            "name": "Treasure Hunt",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run setblock ~ ~ ~ minecraft:chest", "delay": 0},
                {"cmd": "give @r diamond 1", "delay": 5},
                {"cmd": "playsound random.orb @a", "delay": 5}
            ]
        },

        # 11. Spooky Sounds
        {
            "name": "Spooky Sounds",
            "duration": 20,
            "commands": [
                {"cmd": "playsound mob.ghast.scream @a", "delay": 0},
                {"cmd": "playsound ambient.cave @a", "delay": 5},
                {"cmd": f"effect {default_player} blindness 3 1 true", "delay": 2}
            ]
        },

        # 12. Chicken Rain
        {
            "name": "Chicken Rain",
            "duration": 15,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:chicken ~ ~10 ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:chicken ~ ~10 ~5", "delay": 1},
                {"cmd": f"execute as {default_player} run summon minecraft:chicken ~ ~10 ~-5", "delay": 2},
                {"cmd": "playsound mob.chicken.hurt @a", "delay": 0}
            ]
        },

        # 13. TNT Party
        {
            "name": "TNT Party",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:tnt ~ ~ ~5", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:tnt ~ ~ ~-5", "delay": 2},
                {"cmd": f"effect {default_player} resistance 10 255 true", "delay": 0},
                {"cmd": "playsound random.explode @a", "delay": 3}
            ]
        },

        # 14. Instant Arena
        {
            "name": "Instant Arena",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:obsidian", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-5 ~ ~-5 ~5 ~3 ~5 air", "delay": 1},
                {"cmd": f"execute as {default_player} run fill ~-5 ~ ~-5 ~-5 ~3 ~5 minecraft:obsidian", "delay": 2},
                {"cmd": f"execute as {default_player} run fill ~5 ~ ~-5 ~5 ~3 ~5 minecraft:obsidian", "delay": 2},
                {"cmd": f"execute as {default_player} run fill ~-5 ~ ~-5 ~5 ~3 ~-5 minecraft:obsidian", "delay": 2},
                {"cmd": f"execute as {default_player} run fill ~-5 ~ ~5 ~5 ~3 ~5 minecraft:obsidian", "delay": 2},
                {"cmd": "playsound random.anvil_land @a", "delay": 0}
            ]
        },

        # 15. Mob Battle (Fixed NBT tags)
        {
            "name": "Mob Battle",
            "duration": 45,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:zombie ~ ~ ~ {{Team:\"team1\"}}", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:skeleton ~ ~ ~5 {{Team:\"team2\"}}", "delay": 0},
                {"cmd": "effect @e[type=zombie] strength 30 2", "delay": 1},
                {"cmd": "effect @e[type=skeleton] speed 30 2", "delay": 1},
                {"cmd": "playsound mob.zombie.unfect @a", "delay": 0}
            ]
        },

        # 16. Lava Floor
        {
            "name": "Lava Floor",
            "duration": 15,
            "commands": [
                {"cmd": f"effect {default_player} fire_resistance 20 1 true", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:lava", "delay": 2},
                {"cmd": "playsound liquid.lavapop @a", "delay": 1},
                {"cmd": f"execute as {default_player} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 air", "delay": 15}
            ]
        },

        # 17. Ice Age
        {
            "name": "Ice Age",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:ice", "delay": 0},
                {"cmd": f"effect {default_player} slowness 10 2 true", "delay": 0},
                {"cmd": "weather rain", "delay": 1},
                {"cmd": "playsound dig.glass @a", "delay": 0}
            ]
        },

        # 18. Slime Invasion
        {
            "name": "Slime Invasion",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:slime ~ ~ ~ {{Size:3}}", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:slime ~ ~ ~5 {{Size:2}}", "delay": 2},
                {"cmd": f"execute as {default_player} run summon minecraft:slime ~ ~ ~-5 {{Size:1}}", "delay": 4},
                {"cmd": "playsound mob.slime.attack @a", "delay": 0}
            ]
        },

        # 19. Super Jump
        {
            "name": "Super Jump",
            "duration": 15,
            "commands": [
                {"cmd": f"effect {default_player} jump_boost 15 20 true", "delay": 0},
                {"cmd": f"effect {default_player} resistance 15 5 true", "delay": 0},
                {"cmd": f"effect {default_player} slow_falling 15 1 true", "delay": 0},
                {"cmd": "playsound random.levelup @a", "delay": 0}
            ]
        },

        # 20. Disco Party
        {
            "name": "Disco Party",
            "duration": 20,
            "commands": [
                {"cmd": f"effect {default_player} night_vision 20 1 true", "delay": 0},
                {"cmd": f"effect {default_player} speed 20 3 true", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-3 ~3 ~-3 ~3 ~3 ~3 minecraft:glowstone", "delay": 0},
                {"cmd": "playsound note.pling @a", "delay": 1},
                {"cmd": "playsound note.hat @a", "delay": 2},
                {"cmd": "playsound note.bass @a", "delay": 3}
            ]
        },

        # 21. Gift Rain
        {
            "name": "Gift Rain",
            "duration": 15,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:item ~ ~10 ~ minecraft:diamond", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:item ~ ~10 ~ minecraft:gold_ingot", "delay": 2},
                {"cmd": f"execute as {default_player} run summon minecraft:item ~ ~10 ~ minecraft:iron_ingot", "delay": 4},
                {"cmd": "playsound random.orb @a", "delay": 0}
            ]
        },

        # 22. Meteor Shower
        {
            "name": "Meteor Shower",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:fireball ~ ~10 ~ {{direction:[0.0,-1.0,0.0]}}", "delay": 2},
                {"cmd": "playsound fire.ignite @a", "delay": 0},
                {"cmd": f"effect {default_player} fire_resistance 5 1 true", "delay": 1}
            ]
        },

        # 23. Ender Invasion
        {
            "name": "Ender Invasion",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:enderman ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:enderman ~ ~ ~", "delay": 3},
                {"cmd": "playsound mob.endermen.stare @a", "delay": 1},
                {"cmd": f"effect {default_player} invisibility 10 0 true", "delay": 2}
            ]
        },

        # 24. Gravity Flux
        {
            "name": "Gravity Flux",
            "duration": 20,
            "commands": [
                {"cmd": f"effect {default_player} slow_falling 10 1 true", "delay": 0},
                {"cmd": f"effect {default_player} levitation 5 2 true", "delay": 2},
                {"cmd": "playsound item.elytra.fly @a", "delay": 1}
            ]
        },

        # 25. Time Warp
        {
            "name": "Time Warp",
            "duration": 15,
            "commands": [
                {"cmd": f"effect {default_player} speed 15 5 true", "delay": 0},
                {"cmd": f"effect {default_player} slowness 15 5 true", "delay": 5},
                {"cmd": "playsound random.click @a", "delay": 0}
            ]
        },

        # 26. Mystery Box
        {
            "name": "Mystery Box",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run setblock ~ ~ ~ minecraft:chest", "delay": 0},
                {"cmd": "give @r diamond 1", "delay": 3},
                {"cmd": "give @r apple 5", "delay": 3},
                {"cmd": "playsound random.orb @a", "delay": 1}
            ]
        },

        # 27. Ghost Town
        {
            "name": "Ghost Town",
            "duration": 20,
            "commands": [
                {"cmd": "playsound mob.ghast.ambient @a", "delay": 0},
                {"cmd": "playsound ambient.cave @a", "delay": 5},
                {"cmd": f"effect {default_player} blindness 5 1 true", "delay": 2}
            ]
        },

        # 28. Nether Portal Surprise
        {
            "name": "Nether Portal Surprise",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run setblock ~ ~ ~ minecraft:nether_portal", "delay": 0},
                {"cmd": "playsound portal.travel @a", "delay": 1},
                {"cmd": f"execute as {default_player} run summon minecraft:piglin ~ ~ ~", "delay": 3}
            ]
        },

        # 29. Water Spout
        {
            "name": "Water Spout",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:dolphin ~ ~ ~", "delay": 0},
                {"cmd": "playsound ambient.water @a", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:water", "delay": 2}
            ]
        },

        # 30. Shadow Realm
        {
            "name": "Shadow Realm",
            "duration": 30,
            "commands": [
                {"cmd": f"effect {default_player} night_vision 20 1 true", "delay": 0},
                {"cmd": f"effect {default_player} weakness 20 1 true", "delay": 0},
                {"cmd": "playsound mob.wither.ambient @a", "delay": 1}
            ]
        },

        # 31. Trick or Treat
        {
            "name": "Trick or Treat",
            "duration": 15,
            "commands": [
                {"cmd": f"give {default_player} minecraft:pumpkin 1", "delay": 0},
                {"cmd": f"give {default_player} minecraft:coal 3", "delay": 2},
                {"cmd": "playsound random.eat @a", "delay": 1}
            ]
        },

        # 32. Blackout
        {
            "name": "Blackout",
            "duration": 10,
            "commands": [
                {"cmd": f"effect {default_player} blindness 10 1 true", "delay": 0},
                {"cmd": "playsound ambient.weather.lightning.thunder @a", "delay": 0}
            ]
        },

        # 33. Lunar Eclipse
        {
            "name": "Lunar Eclipse",
            "duration": 20,
            "commands": [
                {"cmd": f"effect {default_player} invisibility 20 0 true", "delay": 0},
                {"cmd": "playsound ambient.weather.thunder @a", "delay": 2}
            ]
        },

        # 34. Volcano Eruption
        {
            "name": "Volcano Eruption",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:lava", "delay": 0},
                {"cmd": "playsound random.explode @a", "delay": 2},
                {"cmd": f"execute as {default_player} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:obsidian", "delay": 10}
            ]
        },

        # 35. Corrupted Chunk
        {
            "name": "Corrupted Chunk",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-8 ~-1 ~-8 ~8 ~-1 ~8 minecraft:bedrock", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-8 ~ ~-8 ~8 ~4 ~8 air", "delay": 1},
                {"cmd": "playsound random.anvil_use @a", "delay": 2}
            ]
        },

        # 36. Prismarine Flood
        {
            "name": "Prismarine Flood",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:prismarine", "delay": 0},
                {"cmd": "playsound ambient.underwater.loop @a", "delay": 0}
            ]
        },

        # 37. Emerald Rain
        {
            "name": "Emerald Rain",
            "duration": 15,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:item ~ ~10 ~ minecraft:emerald", "delay": 0},
                {"cmd": "playsound random.orb @a", "delay": 0}
            ]
        },

        # 38. Phantom Wave
        {
            "name": "Phantom Wave",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:phantom ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:phantom ~ ~ ~", "delay": 3},
                {"cmd": "playsound mob.phantom.bite @a", "delay": 1}
            ]
        },

        # 39. Sandstorm
        {
            "name": "Sandstorm",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-10 ~ ~-10 ~10 ~ ~10 minecraft:sand", "delay": 0},
                {"cmd": "weather rain", "delay": 2},
                {"cmd": "playsound ambient.weather.rain @a", "delay": 0}
            ]
        },

        # 40. Berry Explosion
        {
            "name": "Berry Explosion",
            "duration": 15,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-2 ~ ~-2 ~2 ~ ~2 minecraft:sweet_berry_bush", "delay": 0},
                {"cmd": "playsound random.burp @a", "delay": 1}
            ]
        },

        # 41. Glow Worm Swarm
        {
            "name": "Glow Worm Swarm",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:glow_squid ~ ~ ~", "delay": 0},
                {"cmd": "playsound ambient.underwater.loop @a", "delay": 0}
            ]
        },

        # 42. Crop Blitz
        {
            "name": "Crop Blitz",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-5 ~ ~-5 ~5 ~ ~5 minecraft:wheat", "delay": 0},
                {"cmd": "playsound random.burp @a", "delay": 1}
            ]
        },

        # 43. Undead Invasion
        {
            "name": "Undead Invasion",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:zombie ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:skeleton ~ ~ ~", "delay": 2},
                {"cmd": "playsound mob.zombie.say @a", "delay": 1}
            ]
        },

        # 44. Double Drop
        {
            "name": "Double Drop",
            "duration": 15,
            "commands": [
                {"cmd": "gamerule doTileDrops true", "delay": 0},
                {"cmd": "playsound random.successful_hit @a", "delay": 0}
            ]
        },

        # 45. Haunted Tools
        {
            "name": "Haunted Tools",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run give {default_player} minecraft:diamond_pickaxe{{\"Enchantments\":[{{\"id\":\"minecraft:efficiency\",\"lvl\":5}}]}}", "delay": 0},
                {"cmd": "playsound random.anvil_land @a", "delay": 1}
            ]
        },

        # 46. Falling Chests
        {
            "name": "Falling Chests",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:falling_block ~ ~10 ~ {{BlockState:{{Name:\"minecraft:chest\"}}}}", "delay": 0},
                {"cmd": "playsound random.chestopen @a", "delay": 3}
            ]
        },

        # 47. Acid Rain
        {
            "name": "Acid Rain",
            "duration": 20,
            "commands": [
                {"cmd": "weather rain", "delay": 0},
                {"cmd": f"effect {default_player} poison 5 1 true", "delay": 2},
                {"cmd": "playsound ambient.weather.rain @a", "delay": 0}
            ]
        },

        # 48. Twister (Fixed vortex -> minecraft:area_effect_cloud)
        {
            "name": "Twister",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:area_effect_cloud ~ ~ ~ {{Duration:600}}", "delay": 0},
                {"cmd": "playsound mob.endermen.teleport @a", "delay": 1}
            ]
        },

        # 49. Earthquake
        {
            "name": "Earthquake",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:gravel", "delay": 0},
                {"cmd": "playsound block.anvil.land @a", "delay": 1}
            ]
        },

        # 50. One Heart Challenge
        {
            "name": "One Heart Challenge",
            "duration": 60,
            "commands": [
                {"cmd": f"effect {default_player} health_boost 60 2 true", "delay": 0},
                {"cmd": "playsound random.successful_hit @a", "delay": 0}
            ]
        },

        # 51. Zombie Horde (Fixed invalid parameter)
        {
            "name": "Zombie Horde",
            "duration": 35,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:zombie ~ ~ ~", "delay": 0},
                {"cmd": "summon minecraft:zombie ~ ~ ~", "delay": 0.5},
                {"cmd": "playsound mob.zombie.hurt @a", "delay": 1}
            ]
        },

        # 52. Phantom Parade
        {
            "name": "Phantom Parade",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:phantom ~ ~ ~", "delay": 0},
                {"cmd": "playsound mob.phantom.bite @a", "delay": 2}
            ]
        },

        # 53. Trader Surprise
        {
            "name": "Trader Surprise",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:wandering_trader ~ ~ ~", "delay": 0},
                {"cmd": "playsound entity.villager.ambient @a", "delay": 1}
            ]
        },

        # 54. Gamerule Shuffle
        {
            "name": "Gamerule Shuffle",
            "duration": 15,
            "commands": [
                {"cmd": "gamerule doDaylightCycle false", "delay": 0},
                {"cmd": "gamerule doWeatherCycle false", "delay": 1},
                {"cmd": "playsound random.successful_hit @a", "delay": 0}
            ]
        },

        # 55. Creeper Rain
        {
            "name": "Creeper Rain",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:creeper ~ ~10 ~", "delay": 0},
                {"cmd": "playsound random.fuse @a", "delay": 1}
            ]
        },

        # 56. Golden Shower
        {
            "name": "Golden Shower",
            "duration": 15,
            "commands": [
                {"cmd": f"summon minecraft:item ~ ~10 ~ minecraft:gold_nugget", "delay": 0},
                {"cmd": f"summon minecraft:item ~ ~10 ~ minecraft:gold_ingot", "delay": 2},
                {"cmd": "playsound random.orb @a", "delay": 0}
            ]
        },

        # 57. Mystic Fog
        {
            "name": "Mystic Fog",
            "duration": 20,
            "commands": [
                {"cmd": "weather thunder", "delay": 0},
                {"cmd": f"effect {default_player} blindness 5 1 true", "delay": 1},
                {"cmd": "playsound ambient.weather.rain @a", "delay": 2}
            ]
        },

        # 58. Clone Army (Enhanced with armor stand properties)
        {
            "name": "Clone Army",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:armor_stand ~ ~ ~ {{Invisible:1, Marker:1}}", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:armor_stand ~ ~1 ~2 {{Invisible:1, Marker:1}}", "delay": 1},
                {"cmd": f"execute as {default_player} run summon minecraft:armor_stand ~ ~-1 ~-2 {{Invisible:1, Marker:1}}", "delay": 2},
                {"cmd": "playsound random.levelup @a", "delay": 0}
            ]
        },

        # 59. Villager Uprising
        {
            "name": "Villager Uprising",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:villager ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:iron_golem ~ ~ ~", "delay": 2},
                {"cmd": "playsound entity.villager.angry @a", "delay": 1}
            ]
        },

        # 60. Wolf Pack
        {
            "name": "Wolf Pack",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:wolf ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:wolf ~ ~ ~2", "delay": 1},
                {"cmd": "playsound entity.wolf.growl @a", "delay": 0}
            ]
        },

        # 61. Sheep Stampede
        {
            "name": "Sheep Stampede",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:sheep ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:sheep ~ ~ ~2", "delay": 1},
                {"cmd": "playsound entity.sheep.say @a", "delay": 0}
            ]
        },

        # 62. Pillager Patrol
        {
            "name": "Pillager Patrol",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:pillager ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:pillager ~ ~ ~2", "delay": 2},
                {"cmd": "playsound entity.pillager.aggro @a", "delay": 1}
            ]
        },

        # 63. Bee Swarm
        {
            "name": "Bee Swarm",
            "duration": 25,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:bee ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:bee ~ ~ ~2", "delay": 1},
                {"cmd": "playsound entity.bee.loop @a", "delay": 0}
            ]
        },

        # 64. Iron Golem Army
        {
            "name": "Iron Golem Army",
            "duration": 40,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:iron_golem ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:iron_golem ~ ~ ~3", "delay": 2},
                {"cmd": "playsound entity.irongolem.attack @a", "delay": 1}
            ]
        },

        # 65. Wither Warning
        {
            "name": "Wither Warning",
            "duration": 30,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:wither_skeleton ~ ~ ~", "delay": 0},
                {"cmd": "playsound entity.wither.spawn @a", "delay": 2},
                {"cmd": f"effect {default_player} wither 5 1 true", "delay": 1}
            ]
        },

        # 66. Dragon’s Roar
        {
            "name": "Dragon’s Roar",
            "duration": 35,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:ender_dragon ~ ~ ~", "delay": 0},
                {"cmd": "playsound entity.enderdragon.growl @a", "delay": 1},
                {"cmd": f"effect {default_player} slow_falling 10 1 true", "delay": 2}
            ]
        },

        # === NEW EVENTS (67-71) ===
        # 67. Fishing Frenzy
        {
            "name": "Fishing Frenzy",
            "duration": 30,
            "commands": [
                {"cmd": "give @a fishing_rod", "delay": 0},
                {"cmd": "effect @a luck 30 5", "delay": 0},
                {"cmd": "playsound note.pling @a", "delay": 1}
            ]
        },

        # 68. Invisible Maze
        {
            "name": "Invisible Maze",
            "duration": 45,
            "commands": [
                {"cmd": f"execute as {default_player} run fill ~-15 ~ ~-15 ~15 ~4 ~15 minecraft:barrier", "delay": 0},
                {"cmd": f"execute as {default_player} run fill ~-15 ~ ~-15 ~15 ~4 ~15 air replace barrier 50%", "delay": 2},
                {"cmd": "playsound block.piston.extend @a", "delay": 0}
            ]
        },

        # 69. Time Bomb
        {
            "name": "Time Bomb",
            "duration": 20,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:tnt ~ ~ ~", "delay": 0},
                {"cmd": "title @a actionbar §cDetonation in 10 seconds!", "delay": 0},
                {"cmd": "playsound random.click @a", "delay": 10},
                {"cmd": "execute as @a run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 tnt", "delay": 10}
            ]
        },

        # 70. Alchemy Surge
        {
            "name": "Alchemy Surge",
            "duration": 25,
            "commands": [
                {"cmd": "effect @a poison 10 2", "delay": 0},
                {"cmd": "effect @a regeneration 10 2", "delay": 0},
                {"cmd": "effect @a jump_boost 10 5", "delay": 0},
                {"cmd": "playsound block.brewing_stand.brew @a", "delay": 1}
            ]
        },

        # 71. Nether Invasion
        {
            "name": "Nether Invasion",
            "duration": 40,
            "commands": [
                {"cmd": f"execute as {default_player} run summon minecraft:blaze ~ ~ ~", "delay": 0},
                {"cmd": f"execute as {default_player} run summon minecraft:ghast ~ ~5 ~", "delay": 2},
                {"cmd": "weather thunder", "delay": 0},
                {"cmd": "playsound mob.ghast.scream @a", "delay": 1}
            ]
        }
    ]