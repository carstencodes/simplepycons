#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
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


class BigbluebuttonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bigbluebutton"

    @property
    def original_file_name(self) -> "str":
        return "bigbluebutton.svg"

    @property
    def title(self) -> "str":
        return "BigBlueButton"

    @property
    def primary_color(self) -> "str":
        return "#283274"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BigBlueButton</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zM6.838 4.516c.743 0 1.378.364 1.904
 1.091.526.728.787 1.602.787 2.625v6.76c0
 .539.27.809.809.809h4.174c.538 0
 .808-.27.808-.809v-3.205c0-.52-.27-.788-.808-.807h-.807c-1.041-.036-1.923-.308-2.64-.816-.719-.507-1.077-1.133-1.077-1.877h4.524c.97
 0 1.796.342 2.478 1.024a3.374 3.374 0 0 1 1.024 2.476v3.205c0
 .97-.342 1.797-1.024 2.479-.682.682-1.509 1.021-2.478
 1.021h-4.174c-.97 0-1.795-.339-2.477-1.021a3.376 3.376 0 0
 1-1.023-2.479V4.516Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/bigbluebutton/bbb-app-room
s/blob/0fcf9636a3ba683296326f46354265917c4f0ea4/app/assets/images/icon'''

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
