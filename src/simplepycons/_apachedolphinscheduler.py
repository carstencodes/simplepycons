#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class ApacheDolphinschedulerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachedolphinscheduler"

    @property
    def original_file_name(self) -> "str":
        return "apachedolphinscheduler.svg"

    @property
    def title(self) -> "str":
        return "Apache DolphinScheduler"

    @property
    def primary_color(self) -> "str":
        return "#85CDF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache DolphinScheduler</title>
     <path d="M7.9086 1.8777c-1.1454 0-2.073.982-2.073 2.1273 0
 1.2.9276 2.1274 2.073 2.1274h8.3996c1.1454 0 2.072-.982 2.072-2.1274
 0-1.1999-.9266-2.1273-2.072-2.1273zm-4.8545.8725v.9278C1.418 3.787 0
 5.2052 0 6.9505c0 1.7999 1.3631 3.2182 3.1085 3.2182h.5454c.3272 0
 .5454-.2182.5454-.5454 0-.3273-.2182-.5454-.5454-.5454h-.5454c-1.1454
 0-2.0177-.9275-2.0177-2.1274 0-1.1454.8725-2.0728
 1.9633-2.1273v1.1451l1.5276-1.5819Zm4.8545 4.6914c-1.1454
 0-2.073.981-2.073 2.1263 0 1.1454.9276 2.1273 2.073
 2.1273h8.3996c1.1454 0 2.072-.982 2.072-2.1273
 0-1.1454-.9266-2.1263-2.072-2.1263zm12.4903 1.7992c-.3273
 0-.5454.2182-.5454.5455 0 .3272.2181.5454.5454.5454h.5454c1.1454 0
 2.0176.9274 2.0176 2.1273 0 1.1454-.8724 2.0728-1.9633
 2.1274v-1.1452l-1.5276 1.4722 1.5276 1.6363v-.9268c1.6363-.0546
 2.9998-1.4183
 2.9998-3.2182.0546-1.7999-1.3088-3.1639-3.0541-3.1639zm-12.4903
 3.818c-1.1454 0-2.073.982-2.073 2.1273 0 .4364.1097.8723.3824
 1.1995l.491-.163c.5455-.2181 1.1448-.6549
 1.5266-.9822.109-.0545.1638-.1084.2184-.163.0545-.0545.1093-.1094.2184-.164.3272-.2727.7633-.6004
 1.4178-.7095h.3814c.5454 0 1.0363.1639
 1.3636.4911.109-.0545.2181-.1084.2727-.163.1636-.0545.2733-.1638.3824-.2183.109-.0546.272-.1098.4357-.1098.3272
 0 .6545.1639.8181.4911.1091.2182.2186.6006-.1086
 1.2006-.0546.109-.1639.2177-.2184.3814-.1636.3272-.3812.6545-.7084
 1.0908h3.5995c1.1454 0 2.072-.982 2.072-2.1274
 0-1.1999-.9266-2.1816-2.072-2.1816zm-6.4396.0511a.1768.1768 0 0
 0-.0511.0032c-.3273.109-.327.982.2184 1.582.4363.4908.8179.873.8724
 1.2548.1636 1.5272.4915 2.3455 1.2006 3.2182.4908.6 1.1447.927 1.7992
 1.1451.0546-.1636.0552-.3276.1097-.4367.0546-.1091.0544-.2184.0544-.2184l.2183.0554c-.109.5454-.382
 1.6354-.491 1.8536-.1091.3272-.2734.7092.4357.491 1.1453-.3817
 2.0725-1.4726
 2.4543-2.727h.164c-.0545.3272-.1631.6549-.3813.9821.3273-.109.6543-.218.8725-.327.709-.3272
 1.4176-.819 1.7449-1.1462 1.5272-1.4181 2.0724-2.5081
 2.5087-3.2171.4363-.7636-.163-.9818-.4357-.8182-.3272.1091-.7636.4364-1.0908.5454-.2727-.4908-.8186-.7098-1.5276-.6008-.6.1091-.9818.4911-1.3636.7638-.2727.2182-1.1456.9279-1.8546
 1.2006-.7636.3272-1.5268.272-2.0176.163-.2727-.0545-1.418-.5452-.5998-2.236.3818-.8181.3266-1.3631.163-1.4722-.2182-.1636-.8718.3812-1.3081.7084-.358-.2557-1.3879-.751-1.6949-.767Zm8.5126
 2.7857c.1636 0 .2727.1634.2727.327 0 .1637-.109.2725-.2727.327-.1636
 0-.2727-.1633-.2727-.327
 0-.1636.109-.327.2727-.327zm.0543.1086c-.0545 0-.1097.0542-.1097.1087
 0 .0545.0552.1097.1097.1097.0546 0 .1087-.0552.1087-.1097
 0-.0545-.0541-.1087-.1087-.1087zm.2727
 3.4366c-.2727.2182-.6545.4902-1.0908.7084.2727.1636.7631.4363.9268.5454.2727.2182.6001.382.491-.327-.0545-.3273-.1634-.654-.327-.9268z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
