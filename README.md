# ![CC: Python](doc/logo.png)

CC is a mod for Minecraft which adds programmable computers, turtles and more to the game. PolyCC is a way to use a superior programming language 

PolyCC can be installed from [CurseForge]. It requires the [Minecraft Forge][forge] mod loader, but
[versions are available for Fabric][ccrestitched].

## Contributing
Any contribution is welcome, be that using the mod, reporting bugs or contributing code. If you want to get started
developing the mod, [check out the instructions here](CONTRIBUTING.md#developing).

## Using
CC: Tweaked is hosted on my maven repo, and so is relatively simple to depend on. You may wish to add a soft (or hard)
dependency in your `mods.toml` file, with the appropriate version bounds, to ensure that API functionality you depend
on is present.

```groovy
repositories {
  maven {
    url 'https://squiddev.cc/maven/'
    content {
      includeGroup 'org.squiddev'
    }
  }
}

dependencies {
  compileOnly fg.deobf("org.squiddev:cc-tweaked-${mc_version}:${cct_version}:api")
  runtimeOnly fg.deobf("org.squiddev:cc-tweaked-${mc_version}:${cct_version}")
}
```

You should also be careful to only use classes within the `dan200.computercraft.api` package. Non-API classes are
subject to change at any point. If you depend on functionality outside the API, file an issue, and we can look into
exposing more features.

We bundle the API sources with the jar, so documentation should be easily viewable within your editor. Alternatively,
the generated documentation [can be browsed online](https://tweaked.cc/javadoc/).

[computercraft]: https://github.com/dan200/ComputerCraft "ComputerCraft on GitHub"
[PolyCC]: https://github.com/Morgandri1/PolyCC "PolyCC on GitHub"
[forge]: https://files.minecraftforge.net/ "Download Minecraft Forge."
