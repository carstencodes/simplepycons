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


class StagetimerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stagetimer"

    @property
    def original_file_name(self) -> "str":
        return "stagetimer.svg"

    @property
    def title(self) -> "str":
        return "Stagetimer"

    @property
    def primary_color(self) -> "str":
        return "#00A66C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stagetimer</title>
     <path d="M12.127 2.639c0 .821.662 1.475 1.464 1.644a7.832 7.832 0
 0 1 6.201 7.666c0 4.326-3.499 7.833-7.815 7.833a7.767 7.767 0 0
 1-3.932-1.062c-.716-.419-1.66-.372-2.207.253l-.794.906c-.549.625-.491
 1.586.196 2.053A11.946 11.946 0 0 0 11.977 24C18.617 24 24 18.605 24
 11.949 24 5.86 19.495.826 13.644.013c-.829-.116-1.517.571-1.517
 1.411v1.215ZM2.01 15.376c-.8.27-1.236 1.135-.866 1.886.255.518.546
 1.016.871 1.492.473.693 1.449.752
 2.085.202l.921-.797c.636-.551.686-1.502.26-2.224l-.035-.06c-.419-.726-1.277-1.158-2.077-.889l-1.159.39Zm-.322-1.384c-.807.162-1.6-.369-1.658-1.198-.04-.571-.04-1.143
 0-1.714.058-.829.851-1.36 1.658-1.198l1.168.233c.807.162 1.316.957
 1.312 1.788v.068c.004.831-.505 1.626-1.312 1.787l-1.168.234Z" />
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
