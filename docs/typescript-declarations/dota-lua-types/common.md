# Dota Lua common declarations



Shared declarations used by the generated type definitions.

## Contents

<details><summary>Types</summary>

- [__NumberLike](#__numberlike)
- [DotaConstructor](#dotaconstructor)
- [NetworkedData](#networkeddata)

</details>

## Constants

| Name | Type / value | Description |
| --- | --- | --- |
| `vec3_invalid` | `Vector` |  |
| `vec3_origin` | `Vector` |  |

## Type aliases

### __NumberLike

```ts
type __NumberLike = number & Record<Exclude<keyof number, 'toString'>, never>;
```

### DotaConstructor

```ts
type DotaConstructor<T extends object> = {
    [P in keyof T]: P extends '__kind__'
        ? 'constructor'
        : T[P] extends (...args: infer TArgs) => infer TReturn
        ? <TThis extends T>(this: TThis, ...args: TArgs) => TReturn
        : T[P];
};
```

### NetworkedData

```ts
type NetworkedData<T> = T extends string | number
    ? T
    : T extends boolean
    ? 0 | 1
    : T extends (infer U)[]
    ? { [key: number]: NetworkedData<U> }
    : T extends Function // eslint-disable-line @typescript-eslint/ban-types
    ? undefined
    : T extends object
    ? { [K in keyof T]: NetworkedData<T[K]> }
    : never;
```
