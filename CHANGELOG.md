# Changelog

## 2.7.0 (2026-05-03)

Full Changelog: [v2.6.0...v2.7.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.6.0...v2.7.0)

### Features

* **api:** add endpoint specfic timeouts ([15bcc6b](https://github.com/Mozilla-Ocho/tabstack-python/commit/15bcc6b29cf0e64fa5bf544f099471dac26d9cea))
* **automate:** emit task:trace_context SSE event with trace ID ([20d3ff3](https://github.com/Mozilla-Ocho/tabstack-python/commit/20d3ff3b4c5e8d7d287ef9807ecbc33c522bed37))
* support setting headers via env ([4699481](https://github.com/Mozilla-Ocho/tabstack-python/commit/4699481aee8341952e2cae287bc0ff0fc629a292))


### Bug Fixes

* use correct field name format for multipart file arrays ([a10a1ed](https://github.com/Mozilla-Ocho/tabstack-python/commit/a10a1ed1298179229f69dc3c12b899f6242ed1b4))


### Chores

* **internal:** reformat pyproject.toml ([c909f52](https://github.com/Mozilla-Ocho/tabstack-python/commit/c909f52bf36e746213c2cb8b316e6eb1909a2e80))

## 2.6.0 (2026-04-24)

Full Changelog: [v2.5.0...v2.6.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.5.0...v2.6.0)

### Features

* **api:** api update ([6b2a7ab](https://github.com/Mozilla-Ocho/tabstack-python/commit/6b2a7ab3c60534f7347f7e5da4a9dc8c4fa6047e))
* **codegen:** consume Pilo's AutomateStreamEvent as the /automate SSE root ([3615e2d](https://github.com/Mozilla-Ocho/tabstack-python/commit/3615e2dbc4f934ae5b9763b110affc39d04bdce8))

## 2.5.0 (2026-04-22)

Full Changelog: [v2.4.0...v2.5.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.4.0...v2.5.0)

### Features

* **api:** api update ([c43bc04](https://github.com/Mozilla-Ocho/tabstack-python/commit/c43bc047af5b2380a7bbe12a4d2a5825f68b7e48))
* **api:** api update ([2162472](https://github.com/Mozilla-Ocho/tabstack-python/commit/216247282393d0a8d1a4c200a0601766402d3447))


### Bug Fixes

* **codegen:** OAS 3.0 compliance + local Spectral lint + Stainless PR check ([cd8e38c](https://github.com/Mozilla-Ocho/tabstack-python/commit/cd8e38c6bda53419e6fc2bdb33cf251b6498727b))
* **codegen:** reduce Stainless variant-naming and ambiguity warnings ([06f98a5](https://github.com/Mozilla-Ocho/tabstack-python/commit/06f98a5fb555f03d5a467523e5abc6b7e2cad45d))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([0aff4b6](https://github.com/Mozilla-Ocho/tabstack-python/commit/0aff4b62652bf495f02b9b679f11886dc67937b0))


### Chores

* **internal:** more robust bootstrap script ([318ffd3](https://github.com/Mozilla-Ocho/tabstack-python/commit/318ffd399a88d629031487c9652b27850fbeaa16))


### Documentation

* **research:** correct default mode from balanced to fast ([d58bd1b](https://github.com/Mozilla-Ocho/tabstack-python/commit/d58bd1b115a88a89bfdb6cc86a9fc3c53f644764))

## 2.4.0 (2026-04-10)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.3.0...v2.4.0)

### Features

* **api:** add input endpoint ([f3b1f16](https://github.com/Mozilla-Ocho/tabstack-python/commit/f3b1f16204c0d724193815c5e34100831f0a2653))
* **api:** api update ([cda5c19](https://github.com/Mozilla-Ocho/tabstack-python/commit/cda5c19baedee455072a8071cb2741714a9ded19))
* **api:** api update ([ed80ce0](https://github.com/Mozilla-Ocho/tabstack-python/commit/ed80ce06975480e8466b18b75397ee3c761f6398))
* **api:** better handling of SSE events ([6b6ba7b](https://github.com/Mozilla-Ocho/tabstack-python/commit/6b6ba7b5b6a6aba119a6caf6aec3af5ff5c6350b))
* **internal:** implement indices array format for query and form serialization ([97a9bb7](https://github.com/Mozilla-Ocho/tabstack-python/commit/97a9bb7241ad0c7a98483d81f74bbb5ee40e1b93))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([2cda6ae](https://github.com/Mozilla-Ocho/tabstack-python/commit/2cda6aeb86a50115ba347549452c57700e810679))
* **deps:** bump minimum typing-extensions version ([1946504](https://github.com/Mozilla-Ocho/tabstack-python/commit/194650472a951f76bd180e1dd08507fcf2670577))
* ensure file data are only sent as 1 parameter ([10f77bc](https://github.com/Mozilla-Ocho/tabstack-python/commit/10f77bcad1e0ea05151f291bf55b17a04512465a))
* **pydantic:** do not pass `by_alias` unless set ([a32962e](https://github.com/Mozilla-Ocho/tabstack-python/commit/a32962e54563d7073726b4463d70017fc2a40331))
* sanitize endpoint path params ([f4632c7](https://github.com/Mozilla-Ocho/tabstack-python/commit/f4632c74a42a3ea56998e6f9d9afacace4bd4a5c))


### Chores

* **ci:** skip lint on metadata-only changes ([9710840](https://github.com/Mozilla-Ocho/tabstack-python/commit/97108400820fbe715dcb922c997b87b612bf588e))
* configure new SDK language ([f5f587a](https://github.com/Mozilla-Ocho/tabstack-python/commit/f5f587ab07a757e4ada42e6bc3c802f29591c536))
* **internal:** tweak CI branches ([8458777](https://github.com/Mozilla-Ocho/tabstack-python/commit/8458777f42fdbdc611d213513b1e7f026886ba42))
* **internal:** update gitignore ([e39102c](https://github.com/Mozilla-Ocho/tabstack-python/commit/e39102cd8c44fbbaec52a5bed74a11deab25b97f))

## 2.3.0 (2026-03-12)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.2.0...v2.3.0)

### Features

* **api:** api update ([8bb9280](https://github.com/Mozilla-Ocho/tabstack-python/commit/8bb92809a4d7967b25f4a288557d81c9eb6883d9))
* **api:** api update ([2453efd](https://github.com/Mozilla-Ocho/tabstack-python/commit/2453efdf272307fd008f20f18be23be1430795b4))


### Chores

* **ci:** bump uv version ([b17a93a](https://github.com/Mozilla-Ocho/tabstack-python/commit/b17a93a8f667f43518db5a278acf440bfce3ddee))
* **ci:** skip uploading artifacts on stainless-internal branches ([4af1491](https://github.com/Mozilla-Ocho/tabstack-python/commit/4af149100add3389ca29fc7448a49d3b53a7e709))
* format all `api.md` files ([79c09d3](https://github.com/Mozilla-Ocho/tabstack-python/commit/79c09d3d4a871fa902dc4ce0b4153fab01bb1361))
* **internal:** add request options to SSE classes ([36eb33c](https://github.com/Mozilla-Ocho/tabstack-python/commit/36eb33c1ace478eaa0b0489642abc7bc8ba08ad2))
* **internal:** make `test_proxy_environment_variables` more resilient ([e8a44e9](https://github.com/Mozilla-Ocho/tabstack-python/commit/e8a44e9425b78f099a7a3aee65fb25b70c5bce69))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([e9e5e13](https://github.com/Mozilla-Ocho/tabstack-python/commit/e9e5e130d7a2f5b7dd718632673fc8e8d7eb36be))
* **internal:** remove mock server code ([f61d3b4](https://github.com/Mozilla-Ocho/tabstack-python/commit/f61d3b4f5ea74b0da9ec9d2e71b96549361d0ea6))
* **test:** update skip reason message ([911d25f](https://github.com/Mozilla-Ocho/tabstack-python/commit/911d25fcc361fc9cdb00de3684038ca6f5aed55f))
* update mock server docs ([ca0bd54](https://github.com/Mozilla-Ocho/tabstack-python/commit/ca0bd54fc57b5b04db69034124dae1c489926f0d))

## 2.2.0 (2026-02-11)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.1.0...v2.2.0)

### Features

* **api:** rename mcp package ([ad5bd9b](https://github.com/Mozilla-Ocho/tabstack-python/commit/ad5bd9b63e6ec9a242212cbe6cb7fa36903230b4))


### Chores

* **internal:** bump dependencies ([1e58c7b](https://github.com/Mozilla-Ocho/tabstack-python/commit/1e58c7b577422a441286822932d5cb0c30c069fa))
* **internal:** fix lint error on Python 3.14 ([db03056](https://github.com/Mozilla-Ocho/tabstack-python/commit/db030565294dfd9337d44f95260b835098d36b12))

## 2.1.0 (2026-01-30)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v2.0.0...v2.1.0)

### Features

* **api:** add research ([e139b72](https://github.com/Mozilla-Ocho/tabstack-python/commit/e139b72585ff197a48d1af52e7fd8b7ebc5f40d1))
* **api:** api update ([23805e3](https://github.com/Mozilla-Ocho/tabstack-python/commit/23805e34be0a2dc9897a8962a7dd33bd840ef85c))
* **api:** api update ([ac0c746](https://github.com/Mozilla-Ocho/tabstack-python/commit/ac0c74625af51293f79dbca80540781a4589adab))
* **api:** api update ([b8a1e09](https://github.com/Mozilla-Ocho/tabstack-python/commit/b8a1e095bd6153948c18a3b15324fd0166cf136c))
* **api:** api update ([6eb4a9f](https://github.com/Mozilla-Ocho/tabstack-python/commit/6eb4a9feb9f79e9580d5a521de46bb07f23db928))
* **client:** add custom JSON encoder for extended type support ([4b5ce35](https://github.com/Mozilla-Ocho/tabstack-python/commit/4b5ce35a61dcc1e1c60d5d6dbfea22311c663cdb))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([c8fba67](https://github.com/Mozilla-Ocho/tabstack-python/commit/c8fba6725a642e10179f6a0006642f5dfe281c3c))


### Chores

* **ci:** upgrade `actions/github-script` ([b6d62f6](https://github.com/Mozilla-Ocho/tabstack-python/commit/b6d62f664f7cabaa8201fcb02fe50d307e82553c))
* **internal:** update `actions/checkout` version ([9197068](https://github.com/Mozilla-Ocho/tabstack-python/commit/9197068bb9bd06db9e54a49690e25e9c0f93b230))

## 2.0.0 (2026-01-16)

Full Changelog: [v0.0.1...v2.0.0](https://github.com/Mozilla-Ocho/tabstack-python/compare/v0.0.1...v2.0.0)

### Features

* **api:** api update ([5b17ee9](https://github.com/Mozilla-Ocho/tabstack-python/commit/5b17ee90e2ec404df0113d263ea5d90a8a53ed3c))
* **api:** api update ([38f0ce0](https://github.com/Mozilla-Ocho/tabstack-python/commit/38f0ce09eaea36c0b76da30dfd20cbf72846bf68))
* **api:** api update ([db3d6ab](https://github.com/Mozilla-Ocho/tabstack-python/commit/db3d6ab62e77c67e1c1965dd1f9f353effbfdd79))
* **api:** api update ([b3d51f5](https://github.com/Mozilla-Ocho/tabstack-python/commit/b3d51f54ce28b6f46d2b608dc2654072bb13b36b))
* **api:** api update ([b557ea9](https://github.com/Mozilla-Ocho/tabstack-python/commit/b557ea95626e967e5d8d2ec8e533fd16fefceb70))
* **api:** api update ([846fbb1](https://github.com/Mozilla-Ocho/tabstack-python/commit/846fbb18cb5dd2460ba5cfbf1fd7c4b745327d0b))
* **api:** config oidc publishing ([ec742d4](https://github.com/Mozilla-Ocho/tabstack-python/commit/ec742d4bfd382725f91bd28f313f55c270a4500c))
* **api:** config oidc publishing ([61ea691](https://github.com/Mozilla-Ocho/tabstack-python/commit/61ea691ace58aed27900ae5812fae3ac097f8bf9))
* **api:** manual updates ([74c20f3](https://github.com/Mozilla-Ocho/tabstack-python/commit/74c20f386e66ce984850ce1eb8ac208d13d1005f))
* **api:** manual updates ([f7b20ac](https://github.com/Mozilla-Ocho/tabstack-python/commit/f7b20ac87dd24e646176cc5ce6cd0cd3c3759b84))
* **api:** manual updates ([25d4e29](https://github.com/Mozilla-Ocho/tabstack-python/commit/25d4e29291e1ac55840de038bac0e32cd3b150b5))
* **api:** manual updates ([dbfbf9c](https://github.com/Mozilla-Ocho/tabstack-python/commit/dbfbf9c93341b4c01657e3554b283708dee6b047))
* **client:** add support for binary request streaming ([5c8c73a](https://github.com/Mozilla-Ocho/tabstack-python/commit/5c8c73aa8473ce531295da7ef45459648299f778))
* **client:** add support for binary request streaming ([e83b1c6](https://github.com/Mozilla-Ocho/tabstack-python/commit/e83b1c6f03026305f65c511f399057fc3bb92ba7))


### Bug Fixes

* use async_to_httpx_files in patch method ([21f1611](https://github.com/Mozilla-Ocho/tabstack-python/commit/21f1611368ef1e6f8efe1a62a7c56a45e383c7aa))
* use async_to_httpx_files in patch method ([3722dc8](https://github.com/Mozilla-Ocho/tabstack-python/commit/3722dc82196497a2f3984d33b71cdb526e62b609))


### Chores

* **internal:** add `--fix` argument to lint script ([fe8e486](https://github.com/Mozilla-Ocho/tabstack-python/commit/fe8e486950763ba31ddac3ddbf1f0594020e9f2d))
* **internal:** add `--fix` argument to lint script ([4b7bd77](https://github.com/Mozilla-Ocho/tabstack-python/commit/4b7bd771c8acba2537eb5ea40229d8e90e58757b))
* **internal:** codegen related update ([f560cfe](https://github.com/Mozilla-Ocho/tabstack-python/commit/f560cfe29a6d9d2f8578cbc350d43e48b7e4284d))
* **internal:** codegen related update ([4fdb1ce](https://github.com/Mozilla-Ocho/tabstack-python/commit/4fdb1ce6fc5a8d046541c9b86c520097cc295ec8))
* sync repo ([2f19860](https://github.com/Mozilla-Ocho/tabstack-python/commit/2f198600cff3b902bac0e6c743c54bc1ed9618bf))
* sync repo ([03e9ef5](https://github.com/Mozilla-Ocho/tabstack-python/commit/03e9ef53e0e1e88e87d3bfa437e991dcd4a33b2a))
* update SDK settings ([0b77a8b](https://github.com/Mozilla-Ocho/tabstack-python/commit/0b77a8bf3f040a3b942f3156349e640574b166f7))
* update SDK settings ([ccec37e](https://github.com/Mozilla-Ocho/tabstack-python/commit/ccec37e764ed8b4897838ce1ab4159933d4fbbab))
* update SDK settings ([22f2fd5](https://github.com/Mozilla-Ocho/tabstack-python/commit/22f2fd547d5de07a8b1437cab34e2249273f7b6b))
* update SDK settings ([f78675d](https://github.com/Mozilla-Ocho/tabstack-python/commit/f78675dc8a120499a17f89f9f7c0ce61ec350746))
* update SDK settings ([6bdaf91](https://github.com/Mozilla-Ocho/tabstack-python/commit/6bdaf91f5666467d5fd69ad0f916dc6288599576))
* update SDK settings ([92f6785](https://github.com/Mozilla-Ocho/tabstack-python/commit/92f678557fe80699da86a1447801a5b5d54ffdf0))


### Documentation

* add more examples ([1c7a58d](https://github.com/Mozilla-Ocho/tabstack-python/commit/1c7a58dd547c09fa64d9cb8966f04fc2d64a80fd))
* add more examples ([0758a97](https://github.com/Mozilla-Ocho/tabstack-python/commit/0758a9724c7da3b925aad1fedfa1c54967ff3c97))
* prominently feature MCP server setup in root SDK readmes ([ab430a6](https://github.com/Mozilla-Ocho/tabstack-python/commit/ab430a68cb38ee3562bc7a36a15465ddacadc83e))
* prominently feature MCP server setup in root SDK readmes ([64952dc](https://github.com/Mozilla-Ocho/tabstack-python/commit/64952dc16abde02d4247fcc455fb7f6455f38cf0))


### Refactors

* **internal:** switch from rye to uv ([ae82620](https://github.com/Mozilla-Ocho/tabstack-python/commit/ae82620e41334237ed9d7990cbae0d5abc2d0369))
* **internal:** switch from rye to uv ([19b47fc](https://github.com/Mozilla-Ocho/tabstack-python/commit/19b47fc60ff7e09a1a915417772d6a93d9dc1fdd))
