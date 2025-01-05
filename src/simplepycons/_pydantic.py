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


class PydanticIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pydantic"

    @property
    def original_file_name(self) -> "str":
        return "pydantic.svg"

    @property
    def title(self) -> "str":
        return "Pydantic"

    @property
    def primary_color(self) -> "str":
        return "#E92063"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pydantic</title>
     <path d="m23.826
 17.316-4.23-5.866-6.847-9.496c-.348-.48-1.151-.48-1.497 0l-6.845
 9.494-4.233 5.868a.925.925 0 0 0 .46 1.417l11.078 3.626h.002a.92.92 0
 0 0 .572 0h.002l11.077-3.626c.28-.092.5-.31.59-.592a.916.916 0 0
 0-.13-.825h.002ZM12.001 4.07l4.44
 6.158-4.152-1.36c-.032-.01-.066-.008-.098-.016a.8.8 0 0
 0-.096-.016c-.032-.004-.062-.016-.094-.016s-.062.012-.094.016a.74.74
 0 0 0-.096.016c-.032.006-.066.006-.096.016L7.59 10.221l-.026.008
 4.44-6.158h-.002Zm-6.273 8.7 4.834-1.583.516-.168v9.19L2.41
 17.372l3.317-4.6Zm7.197 7.437V11.02l5.35 1.752 3.316 4.598-8.666
 2.838Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pydantic/pydantic/blob/94c'''

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
