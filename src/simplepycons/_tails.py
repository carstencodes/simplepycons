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


class TailsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tails"

    @property
    def original_file_name(self) -> "str":
        return "tails.svg"

    @property
    def title(self) -> "str":
        return "Tails"

    @property
    def primary_color(self) -> "str":
        return "#56347C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tails</title>
     <path d="M21.356 11.162v3.98c0
 .122-.081.154-.181.071l-2.032-1.682a.55.55 0 0
 1-.181-.37v-.501l-.635-.516c-.68-.554-1.226-1.677-1.226-2.5
 0-.822.549-1.036
 1.226-.478l.635.516V9.18c0-.122.081-.154.181-.071l2.032
 1.682c.1.082.181.248.181.37zm-2.993-1.265c-.358-.296-.648-.182-.648.253s.29
 1.027.648 1.323l.599.486v-1.576l-.599-.486zM21.202
 19.934l.013-.01a.334.334 0 0 0 .037-.036l.004-.004a.36.36 0 0 0
 .032-.046l.007-.013a.299.299 0 0 0 .019-.042l.004-.01a.329.329 0 0 0
 .013-.055v-.014l.003-.027.003-.152-5.223-4.28.022-12.91-.147-.111-.004-.003-.034-.02c-.007-.004-.014-.01-.022-.013l-.03-.01c-.01-.004-.02-.009-.03-.011l-.026-.004c-.013-.002-.026-.005-.039-.005H15.8l-.023.001c-.013
 0-.025.001-.037.003l-.03.007c-.01.003-.021.005-.031.01-.01.003-.02.008-.029.012l-.029.015a.202.202
 0 0 0-.014.01c-.012.004-.024.007-.035.013l-3.444 1.726.72.57.027
 10.067-5.246-4.32-.003-5.241L7.623.328l-.001-.01a.283.283 0 0
 0-.004-.035c-.001-.01-.002-.02-.005-.03L7.605.223C7.6.213 7.597.201
 7.59.19L7.588.181l-.01-.015c-.006-.01-.012-.021-.02-.031L7.54.112A.354.354
 0 0 0 7.466.05.294.294 0 0 0
 7.44.035c-.01-.004-.02-.01-.03-.013a.365.365 0 0
 0-.061-.016L7.314.002 7.294 0l-.009.001a.3.3 0 0
 0-.036.004c-.01.001-.02.002-.03.005-.01.002-.019.006-.029.009a.286.286
 0 0 0-.033.012l-.009.004L2.825 2.2l-.016.01a.336.336 0 0
 0-.077.061.303.303 0 0 0-.053.078.402.402 0 0 0-.023.06.284.284 0 0
 0-.01.065c-.001.006-.003.013-.002.02l.006 10.108v.02l.002.008c0
 .015.003.03.006.044l.002.009.004.011a.32.32 0 0 0
 .02.054v.001h.001c.009.018.02.034.031.05l.007.01.006.006a.31.31 0 0 0
 .031.032l.006.006c.004.003.008.005.01.008.002 0 .003.003.005.004l4.7
 3.909-.107 2.673v.038l.004.025.002.015c0 .005.002.01.004.015 0
 .004.002.007.003.011l.001.005.003.01c.005.014.01.028.017.04v.002a.32.32
 0 0 0 .031.049l.006.008.005.005a.342.342 0 0 0
 .037.039l.005.003.003.002.003.004 5.317
 4.212c.1.078.236.092.35.035l7.988-4 .004-.002a.321.321 0 0 0
 .045-.029zM5.475 10.985L3.819 9.706v1.1l.844.585-1.392.698-.006-9.376
 2.176-1.09.023 2.392-1.546-1.236v1.1l1.554 1.235.024 1.182L3.901
 5.02v1.1l1.603 1.275-.006 1.283-1.573-1.257v1.1l1.58 1.256.01
 1.187zm3.433 6.038l-5.309-4.365 3.668-1.837 5.309 4.365zM6.123
 1.282l.733-.367.079 9.34-.733.366zM8.617 8.396l-.001-1.59L9.925
 7.83l.001 1.591zM9.926 6.568l-1.31-1.025V3.952l1.309 1.025zM11.018
 5.816c.507.646 1.026 1.907 1.026 3.073 0 1.165-.519 1.562-1.026
 1.362V5.816z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://tails.boum.org/contribute/how/promote'''

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
