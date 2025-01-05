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


class FastapiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fastapi"

    @property
    def original_file_name(self) -> "str":
        return "fastapi.svg"

    @property
    def title(self) -> "str":
        return "FastAPI"

    @property
    def primary_color(self) -> "str":
        return "#009688"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FastAPI</title>
     <path d="M12 .0387C5.3729.0384.0003 5.3931 0 11.9988c-.001 6.6066
 5.372 11.9628 12 11.9625 6.628.0003 12.001-5.3559
 12-11.9625-.0003-6.6057-5.3729-11.9604-12-11.96m-.829
 5.4153h7.55l-7.5805 5.3284h5.1828L5.279 18.5436q2.9466-6.5444
 5.892-13.0896" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tiangolo/fastapi/blob/ffb4'''

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
