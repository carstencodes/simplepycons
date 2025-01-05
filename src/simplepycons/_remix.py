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


class RemixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "remix"

    @property
    def original_file_name(self) -> "str":
        return "remix.svg"

    @property
    def title(self) -> "str":
        return "Remix"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Remix</title>
     <path d="M21.511 18.508c.216 2.773.216 4.073.216
 5.492H15.31c0-.309.006-.592.011-.878.018-.892.036-1.821-.109-3.698-.19-2.747-1.374-3.358-3.55-3.358H1.574v-5h10.396c2.748
 0 4.122-.835 4.122-3.049
 0-1.946-1.374-3.125-4.122-3.125H1.573V0h11.541c6.221 0 9.313 2.938
 9.313 7.632 0 3.511-2.176 5.8-5.114 6.182 2.48.497 3.93 1.909 4.198
 4.694ZM1.573 24v-3.727h6.784c1.133 0 1.379.84 1.379 1.342V24Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://drive.google.com/drive/u/0/folders/1p'''

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
