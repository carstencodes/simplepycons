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


class ImmerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "immer"

    @property
    def original_file_name(self) -> "str":
        return "immer.svg"

    @property
    def title(self) -> "str":
        return "Immer"

    @property
    def primary_color(self) -> "str":
        return "#00E7C3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Immer</title>
     <path d="M2.2706 14.3327C1.0174 14.3327 0 13.3149 0
 12.0612s1.0174-2.2714 2.2706-2.2714 2.2706 1.0178 2.2706
 2.2714-1.0175 2.2715-2.2706 2.2715zm19.4594.8587a3.1215 3.1215 0 0
 1-1.8217-.5845c-.7428.8369-1.0466 1.047-2.0669 1.047-1.5417
 0-3.1201-2.3208-4.5579-4.3146 1.4966-2.3358 2.8703-3.8786
 4.3307-3.8786 1.1153 0 2.1849.4937 2.7865 1.7668a3.1155 3.1155 0 0 1
 1.3291-.2958 3.1051 3.1051 0 0 1
 1.1697.2262c-.88-2.5989-2.9964-3.9134-5.1127-3.9134-2.3344 0-4.0593
 2.16-5.5753 4.6292-1.7833-2.4318-3.4838-4.6292-5.9239-4.6292-2.0769
 0-4.154 1.2863-5.0431 3.8295a3.1179 3.1179 0 0 1 .9355-.1423 3.113
 3.113 0 0 1 1.7177.5139c.546-.7723 1.2454-1.2347 2.0074-1.2095
 1.5368.0516 2.9282 1.8499 4.6866 4.3248-1.2802 1.9587-2.9227
 3.8683-4.3102 3.8683-1.0566 0-2.0739-.4443-2.6895-1.5742a3.1139
 3.1139 0 0 1-1.412.3362c-.371.0066-.7336-.0773-1.085-.1857.9316 2.417
 2.9722 3.6396 5.0129 3.6396 2.326 0 3.9314-2.0555 5.5251-4.6143
 1.7485 2.4637 3.4992 4.7244 5.9921 4.7244 2.0245 0 4.2973-1.3328
 5.2229-3.7499-.3583.0875-.7236.1989-1.118.1861zm-.0006-5.4016c-1.2531
 0-2.2705 1.0178-2.2705 2.2714s1.0174 2.2715 2.2705 2.2715c1.2532 0
 2.2706-1.0178 2.2706-2.2715s-1.0174-2.2714-2.2706-2.2714z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/immerjs/immer/blob/7a53828'''

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
