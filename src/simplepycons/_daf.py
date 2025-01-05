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


class DafIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "daf"

    @property
    def original_file_name(self) -> "str":
        return "daf.svg"

    @property
    def title(self) -> "str":
        return "DAF"

    @property
    def primary_color(self) -> "str":
        return "#00529B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DAF</title>
     <path d="M19.649
 12.782h-2.643V8.723H24v1.183h-4.351v.723h4.277v1.147h-4.277zm-7.51-3.039l-1.831
 3.05H7.76l2.414-4.07h3.924l2.424 4.07h-5.364l.64-1.06h1.534zM.004
 12.785V8.741h4.99c1.62 0 2.773.738 2.773 1.994 0 1.196-.914 2.05-2.82
 2.05zm4.008-1.034c.621 0 .985-.53.985-.935
 0-.413-.325-.896-.967-.896H2.671v1.831zM0 13.731h23.926v1.546H0Z" />
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
