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


class LitiengineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "litiengine"

    @property
    def original_file_name(self) -> "str":
        return "litiengine.svg"

    @property
    def title(self) -> "str":
        return "LITIENGINE"

    @property
    def primary_color(self) -> "str":
        return "#00A5BC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LITIENGINE</title>
     <path d="m0 12.018 2.09 2.088L11.987 24l2.146-2.146-9.897-9.893
 6.586-6.582-2.09-2.089Zm13.211 6.624 2.08 2.078
 5.425-5.422-2.08-2.078zM9.85 2.151l6.606 6.602L9.9 15.306l2.134 2.133
 6.555-6.553 3.258 3.257L24 11.993 12 0Zm-3.276 9.853 2.035 2.034
 5.453-5.45-2.035-2.035z" />
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
