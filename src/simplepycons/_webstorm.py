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


class WebstormIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webstorm"

    @property
    def original_file_name(self) -> "str":
        return "webstorm.svg"

    @property
    def title(self) -> "str":
        return "WebStorm"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WebStorm</title>
     <path d="M0 0v24h24V0H0zm17.889 2.889c1.444 0 2.667.444 3.667
 1.278l-1.111
 1.667c-.889-.611-1.722-1-2.556-1s-1.278.389-1.278.889v.056c0
 .667.444.889 2.111 1.333 2 .556 3.111 1.278 3.111 3v.056c0 2-1.5
 3.111-3.611 3.111-1.5-.056-3-.611-4.167-1.667l1.278-1.556c.889.722
 1.833 1.222 2.944 1.222.889 0 1.389-.333
 1.389-.944v-.056c0-.556-.333-.833-2-1.278-2-.5-3.222-1.056-3.222-3.056v-.056c0-1.833
 1.444-3 3.444-3zm-16.111.222h2.278l1.5 5.778 1.722-5.778h1.667l1.667
 5.778 1.5-5.778h2.333l-2.833 9.944H9.723L8.112 7.277l-1.667
 5.778H4.612L1.779 3.111zm.5 16.389h9V21h-9v-1.5z" />
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
