# Panorama common declarations



Shared declarations used by the generated type definitions.

## Contents

<details><summary>Types</summary>

- [AbilityEntityIndex](#abilityentityindex)
- [BuffID](#buffid)
- [EntityIndex](#entityindex)
- [GameEventListenerID](#gameeventlistenerid)
- [HeroID](#heroid)
- [ItemEntityIndex](#itementityindex)
- [NetTableListenerID](#nettablelistenerid)
- [ParticleID](#particleid)
- [PlayerID](#playerid)
- [ScheduleID](#scheduleid)
- [UnhandledEventListenerID](#unhandledeventlistenerid)

</details>

## Type aliases

### AbilityEntityIndex

```ts
type AbilityEntityIndex = EntityIndex & { _abilityEntityIndex: never };
```

### BuffID

```ts
type BuffID = number & { readonly __tag__: 'BuffID' };
```

### EntityIndex

```ts
type EntityIndex = number & { _entityIndex: never };
```

### GameEventListenerID

```ts
type GameEventListenerID = number & { readonly __tag__: 'GameEventListenerID' };
```

### HeroID

```ts
type HeroID = number & { readonly __tag__: 'HeroID' };
```

### ItemEntityIndex

```ts
type ItemEntityIndex = AbilityEntityIndex & { _itemEntityIndex: never };
```

### NetTableListenerID

```ts
type NetTableListenerID = number & { readonly __tag__: 'NetTableListenerID' };
```

### ParticleID

```ts
type ParticleID = number & { readonly __tag__: 'ParticleID' };
```

### PlayerID

```ts
type PlayerID =
    | -1
    | 0
    | 1
    | 2
    | 3
    | 4
    | 5
    | 6
    | 7
    | 8
    | 9
    | 10
    | 11
    | 12
    | 13
    | 14
    | 15
    | 16
    | 17
    | 18
    | 19
    | 20
    | 21
    | 22
    | 23;
```

### ScheduleID

```ts
type ScheduleID = number & { readonly __tag__: 'ScheduleID' };
```

### UnhandledEventListenerID

```ts
type UnhandledEventListenerID = number & { readonly __tag__: 'UnhandledEventListenerID' };
```
