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


class NatsdotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "natsdotio"

    @property
    def original_file_name(self) -> "str":
        return "natsdotio.svg"

    @property
    def title(self) -> "str":
        return "NATS.io"

    @property
    def primary_color(self) -> "str":
        return "#27AAE1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NATS.io</title>
     <path d="M12.004 0H.404v18.807h9.938l1.714 1.602v-.026L15.966
 24v-5.193h7.63V0H12.003zm7.578 14.45H15.38L6.898
 6.519v7.93H4.116V4.376h4.349l8.344 7.784V4.375h2.773V14.45z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cncf/artwork/blob/88bc5e7a
0cc7f3770ba6edddc92e1ab8a6006171/projects/nats/icon/black/nats-icon-bl'''

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
