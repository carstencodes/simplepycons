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


class AffinityPhotoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "affinityphoto"

    @property
    def original_file_name(self) -> "str":
        return "affinityphoto.svg"

    @property
    def title(self) -> "str":
        return "Affinity Photo"

    @property
    def primary_color(self) -> "str":
        return "#4E3188"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Affinity Photo</title>
     <path d="M24 2.344v19.312A2.345 2.345 0 0 1 21.656 24H2.344A2.345
 2.345 0 0 1 0 21.656V2.344A2.345 2.345 0 0 1 2.344 0h19.312A2.345
 2.345 0 0 1 24 2.344Zm-13.328-.586-.41.709 5.021 8.693
 5.43-9.402H10.672Zm2.213 7.702H11.12a.901.901 0 0 0-.75.446l-.925
 1.605-.007.011a.901.901 0 0 0 0 .872l.924 1.599.01.017a.893.893 0 0 0
 .755.428c.002 0 1.178.001 1.765-.002a.888.888 0 0 0
 .75-.436c.311-.539.624-1.077.933-1.617a.879.879 0 0
 0-.006-.863l-.008-.013-.921-1.595-.005-.008a.897.897 0 0
 0-.75-.444ZM2.36 22.18 9.699 9.475H6.215l-4.457 7.717.002
 4.182a.94.94 0 0 0 .6.806Zm11.844.062-5.479-9.486-5.485
 9.486h10.964ZM12.926 8.676l-3.125-5.41-3.125 5.41h6.25Zm9.316
 6.56H11.08l4.046 7.006h6.197a.938.938 0 0 0
 .919-.937v-6.069Zm-.635-13.428-7.295 12.63h7.93V2.695a.938.938 0 0
 0-.635-.887Z" />
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
