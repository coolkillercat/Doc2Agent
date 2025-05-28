### StepManeuver object

**Properties**

- `location`: A `[longitude, latitude]` pair describing the location of the turn.
- `bearing_before`: The clockwise angle from true north to the
direction of travel immediately before the maneuver.
- `bearing_after`: The clockwise angle from true north to the
direction of travel immediately after the maneuver.
- `type` A string indicating the type of maneuver. **new identifiers might be introduced without API change**
Types unknown to the client should be handled like the `turn` type, the existance of correct `modifier` values is guranteed.

| `type` | Description |
| --- | --- |
| `turn` | a basic turn into direction of the `modifier` |
| `new name` | no turn is taken/possible, but the road name changes. The road can take a turn itself, following `modifier` . |
| `depart` | indicates the departure of the leg |
| `arrive` | indicates the destination of the leg |
| `merge` | merge onto a street (e.g. getting on the highway from a ramp, the `modifier specifies the direction of the merge` ) |
| `ramp` | **Deprecated** . Replaced by `on_ramp` and `off_ramp` . |
| `on ramp` | take a ramp to enter a highway (direction given my `modifier` ) |
| `off ramp` | take a ramp to exit a highway (direction given my `modifier` ) |
| `fork` | take the left/right side at a fork depending on `modifier` |
| `end of road` | road ends in a T intersection turn in direction of `modifier` |
| `use lane` | going straight on a specific lane |
| `continue` | Turn in direction of `modifier` to stay on the same road |
| `roundabout` | traverse roundabout, has additional field `exit` with NR if the roundabout is left. `the modifier specifies the direction of entering the roundabout` |
| `rotary` | a traffic circle. While very similar to a larger version of a roundabout, it does not necessarily follow roundabout rules for right of way. It can offer `rotary_name/rotary_pronunciation` in addition to the `exit` parameter. |
| `roundabout turn` | Describes a turn at a small roundabout that should be treated as normal turn. The `modifier` indicates the turn direciton. Example instruction: `At the roundabout turn left` . |
| `notification` | not an actual turn but a change in the driving conditions. For example the travel mode. If the road takes a turn itself, the `modifier` describes the direction |

Please note that even though there are `new name` and `notification` instructions, the `mode` and `name` can change
between all instructions. They only offer a fallback in case nothing else is to report.

- `modifier` An optional `string` indicating the direction change of the maneuver.

| `modifier` | Description |
| --- | --- |
| `uturn` | indicates reversal of direction |
| `sharp right` | a sharp right turn |
| `right` | a normal turn to the right |
| `slight right` | a slight turn to the right |
| `straight` | no relevant change in direction |
| `slight left` | a slight turn to the left |
| `left` | a normal turn to the left |
| `sharp left` | a sharp turn to the left |

The list of turns without a modifier is limited to: `depart/arrive`. If the source/target location is close enough to the `depart/arrive` location, no modifier will be given.

The meaning depends on the `type` field.

| `type` | Description |
| --- | --- |
| `turn` | `modifier` indicates the change in direction accomplished through the turn |
| `depart` / `arrive` | `modifier` indicates the position of departure point and arrival point in relation to the current direction of travel |

- `exit` An optional `integer` indicating number of the exit to take. The field exists for the following `type` field:

| `type` | Description |
| --- | --- |
| `roundabout` / `rotary` | Number of the roundabout exit to take. If exit is `undefined` the destination is on the roundabout. |
| else | Indicates the number of intersections passed until the turn. Example instruction: `at the fourth intersection, turn left` |

New properties (potentially depending on `type`) may be introduced in the future without an API version change.